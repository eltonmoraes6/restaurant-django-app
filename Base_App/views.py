from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as AuthLoginView
from django.core.mail import send_mail
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from Base_App.models import (AboutUs, BookTable, Cart, Feedback, ItemList,
                             Items, Order, OrderItem, PageSection, User)

from .forms import ItemsForm, PageSectionForm

# -------------------------------
# CART SYSTEM (SESSION + DB FIX)
# -------------------------------


def add_to_cart(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"message": "Please log in to add items to cart."}, status=403)

        item_id = request.POST.get("item_id")
        item = get_object_or_404(Items, id=item_id)

        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            item=item,
        )

        # If new: quantity should start at 1
        if created:
            cart_item.quantity = 1
        else:
            cart_item.quantity += 1  # optional: increase quantity on repeated add

        cart_item.save()

        return JsonResponse({"message": f"{item.Item_name} added to cart!"})

    return JsonResponse({"message": "Invalid request"}, status=400)



def get_cart_items(request):
    """ Used by Base.html modal popup """
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    cart_items = Cart.objects.filter(user=request.user).select_related('item')

    items = [{
        'name': c.item.Item_name,
        'quantity': c.quantity,
        'price': c.item.Price,
        'total': c.quantity * c.item.Price
    } for c in cart_items]

    return JsonResponse({'items': items})


# -------------------------------
# LOGIN / LOGOUT / SIGNUP
# -------------------------------

class LoginView(AuthLoginView):
    template_name = 'login.html'

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('admin:index')
        return reverse_lazy('Home')


def LogoutView(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("Home")


def SignupView(request):
    """ Handles signup inside login.html with tab switching """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('Home')

        messages.error(request, "Signup error. Please try again.")

    else:
        form = UserCreationForm()

    return render(request, 'login.html', {
        'form': form,
        'tab': 'signup'
    })


# -------------------------------
# PAGE VIEWS
# -------------------------------

def HomeView(request):
    return render(request, 'home.html', {
        'items': Items.objects.all(),
        'list': ItemList.objects.all(),
        'review': Feedback.objects.all().order_by('-id')[:5]
    })


def AboutView(request):
    return render(request, 'about.html', {
        'data': AboutUs.objects.all()
    })


def MenuView(request):
    return render(request, 'menu.html', {
        'items': Items.objects.all(),
        'list': ItemList.objects.all()
    })


# -------------------------------
# BOOK TABLE
# -------------------------------

def BookTableView(request):
    google_maps_api_key = settings.GOOGLE_MAPS_API_KEY

    if request.method == 'POST':
        name = request.POST.get('user_name')
        phone = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        persons = request.POST.get('total_person')
        date = request.POST.get('booking_data')

        # Simple server-side validation
        if name and phone and email and persons and date:
            booking = BookTable(
                Name=name,
                Phone_number=phone,
                Email=email,
                Total_person=persons,
                Booking_date=date
            )
            booking.save()

            # Email Notification
            subject = "Booking Confirmation"
            message = (
                f"Hello {name},\n\n"
                f"Your booking has been confirmed!\n"
                f"Guests: {persons}\n"
                f"Date: {date}\n\n"
                f"Thank you for choosing us!"
            )

            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

            messages.success(request, "Booking confirmed! Check your email.")
            return redirect('Book_Table')

        messages.error(request, "Please fill all fields correctly.")

    return render(request, 'book_table.html', {
        'google_maps_api_key': google_maps_api_key
    })


# -------------------------------
# FEEDBACK
# -------------------------------

def FeedbackView(request):
    if request.method == 'POST':
        name = request.POST.get('User_name')
        desc = request.POST.get('Description')
        rating = request.POST.get('Rating')
        image = request.FILES.get('Selfie')

        if name:
            Feedback.objects.create(
                User_name=name,
                Description=desc,
                Rating=rating,
                Image=image
            )

            messages.success(request, "Feedback submitted successfully!")
            return redirect('Feedback_Form')

    return render(request, 'feedback.html')


def CartPageView(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = Cart.objects.filter(user=request.user)
    total = sum(c.quantity * c.item.Price for c in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })


def RemoveCartItem(request, id):
    cart_item = get_object_or_404(Cart, id=id, user=request.user)
    cart_item.delete()
    return redirect('Cart')


def CartPageView(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = Cart.objects.filter(user=request.user)
    total = sum(c.quantity * c.item.Price for c in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })


def ConfirmOrder(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        return redirect('Cart')

    total = sum(c.quantity * c.item.Price for c in cart_items)

    order = Order.objects.create(user=request.user, total=total, is_paid=True)

    for c in cart_items:
        OrderItem.objects.create(
            order=order,
            item=c.item,
            quantity=c.quantity,
            price=c.item.Price
        )

    cart_items.delete()

    return redirect('OrderSuccess', order_id=order.id)


def FakePaymentView(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        return redirect('Cart')

    total = sum(c.quantity * c.item.Price for c in cart_items)

    return render(request, 'fake_payment.html', {
        'total': total
    })

def OrderSuccessView(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = order.items.all()

    return render(request, 'order_success.html', {
        'order': order,
        'items': items
    })

def CheckoutPageView(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        messages.error(request, "Your cart is empty.")
        return redirect('Cart')

    total = sum(c.quantity * c.item.Price for c in cart_items)

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total
    })


@login_required
def UserProfileView(request):
    user = request.user
    orders = Order.objects.filter(user=user).order_by('-created_at')

    return render(request, 'profile.html', {
        'user': user,
        'orders': orders
    })

@login_required
def MyOrdersView(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'my_orders.html', {
        'orders': orders
    })

@staff_member_required
def AdminDashboardView(request):

    total_users = User.objects.count()
    total_orders = Order.objects.count()
    total_revenue = Order.objects.filter(is_paid=True).aggregate(Sum('total'))['total__sum'] or 0
    pending_orders = Order.objects.filter(is_paid=False).count()
    last_orders = Order.objects.order_by('-created_at')[:10]

    return render(request, 'admin_dashboard.html', {
        'total_users': total_users,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'pending_orders': pending_orders,
        'last_orders': last_orders,
    })

def increase_quantity(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect("Cart")


def decrease_quantity(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        # If quantity would go below 1, remove item from cart
        cart_item.delete()

    return redirect("Cart")

@login_required
@user_passes_test(lambda u: u.is_staff)
def cms_list(request):
    content = PageSection.objects.all().order_by("page", "section")
    return render(request, "cms_list.html", {"content": content})

@login_required
@user_passes_test(lambda u: u.is_staff)
def cms_create(request):
    if request.method == "POST":
        form = PageSectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cms_list")
    else:
        form = PageSectionForm()
    return render(request, "cms_form.html", {"form": form, "title": "Create New CMS Section"})

@login_required
@user_passes_test(lambda u: u.is_staff)
def cms_edit(request, pk):
    section = get_object_or_404(PageSection, pk=pk)
    if request.method == "POST":
        form = PageSectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            return redirect("cms_list")
    else:
        form = PageSectionForm(instance=section)
    return render(request, "cms_form.html", {"form": form, "title": "Edit CMS Section"})

@login_required
@user_passes_test(lambda u: u.is_staff)
def items_list(request):
    items = Items.objects.all().order_by("-id")
    return render(request, "items_list.html", {"items": items})


@login_required
@user_passes_test(lambda u: u.is_staff)
def items_create(request):
    if request.method == "POST":
        form = ItemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("items_list")
    else:
        form = ItemsForm()

    return render(request, "items_form.html", {"form": form, "title": "Add Product"})


@login_required
@user_passes_test(lambda u: u.is_staff)
def items_edit(request, pk):
    item = get_object_or_404(Items, pk=pk)

    if request.method == "POST":
        form = ItemsForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("items_list")
    else:
        form = ItemsForm(instance=item)

    return render(request, "items_form.html", {"form": form, "title": "Edit Product"})

@login_required
@user_passes_test(lambda u: u.is_staff)
def order_list(request):
    orders = Order.objects.all().order_by("-created_at")
    return render(request, "order_list.html", {"orders": orders})
