from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Base_App.views import (AboutView, AdminDashboardView, BookTableView,
                            CartPageView, CheckoutPageView, ConfirmOrder,
                            FakePaymentView, FeedbackView, HomeView, LoginView,
                            LogoutView, MenuView, MyOrdersView,
                            OrderSuccessView, RemoveCartItem, SignupView,
                            UserProfileView, add_to_cart, decrease_quantity,
                            get_cart_items, increase_quantity)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView, name='signup'),
    path('logout/', LogoutView, name='logout'),

    # Pages
    path('', HomeView, name='Home'),
    path('menu/', MenuView, name='Menu'),
    path('about/', AboutView, name='About'),
    path('book_table/', BookTableView, name='Book_Table'),
    path('feedback/', FeedbackView, name='Feedback_Form'),

    # Cart
    path('cart/', CartPageView, name='Cart'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('get-cart-items/', get_cart_items, name='get_cart_items'),
    path('remove-cart/<int:id>/', RemoveCartItem, name='RemoveCart'),

    # Checkout
    path('checkout/', CheckoutPageView, name='Checkout'),
    path('confirm-order/', ConfirmOrder, name='ConfirmOrder'),
    path('payment/', FakePaymentView, name='FakePayment'),
    path('order-success/<int:order_id>/', OrderSuccessView, name='OrderSuccess'),

    path('profile/', UserProfileView, name='user_profile'),
    path('my-orders/', MyOrdersView, name='my_orders'),
    path('admin-dashboard/', AdminDashboardView, name='admin_dashboard'),

    path("increase/<int:cart_id>/", increase_quantity, name="increase_quantity"),
    path("decrease/<int:cart_id>/", decrease_quantity, name="decrease_quantity"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
