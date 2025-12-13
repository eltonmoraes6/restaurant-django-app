from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Base_App.views import add_category
from django.shortcuts import redirect

from Base_App.views import (AboutView, AdminDashboardView, BookTableView,
                            CartPageView, CheckoutPageView, ConfirmOrder,
                            FakePaymentView, FeedbackView, HomeView, LoginView,
                            LogoutView, MenuView, MyOrdersView,
                            OrderSuccessView, RemoveCartItem, SignupView,
                            UserProfileView, add_to_cart,
                            assign_delivery_person, cms_create, cms_edit,
                            cms_list, decrease_quantity, delivery_detail,
                            delivery_list, delivery_person_create,
                            delivery_person_list, delivery_update,
                            get_cart_items, increase_quantity, items_create,
                            items_edit, items_list, logistics_dashboard,
                            logistics_order_detail, order_list,
                            update_delivery_status)

urlpatterns = [
    path('admin/', admin.site.urls),

    # CUSTOM ADMIN PANEL
    path("dashboard/items/", items_list, name="items_list"),
    path("dashboard/items/add/", items_create, name="item_add"),
    path("dashboard/items/edit/<int:pk>/", items_edit, name="item_edit"),

    path("dashboard/orders/", order_list, name="order_list"),
    #added category urls
    path("/admin/Base_App/category/add/", items_create, name="category_add"),
    # ADICIONE ESSA LINHA
    path("dashboard/category/add/", add_category, name="category_add"),


    # CMS
    path("cms/", cms_list, name="cms_list"),
    path("cms/create/", cms_create, name="cms_create"),
    path("cms/edit/<int:pk>/", cms_edit, name="cms_edit"),

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

    # Profile
    path('profile/', UserProfileView, name='user_profile'),
    path('my-orders/', MyOrdersView, name='my_orders'),
    path('admin-dashboard/', AdminDashboardView, name='admin_dashboard'),

    path("increase/<int:cart_id>/", increase_quantity, name="increase_quantity"),
    path("decrease/<int:cart_id>/", decrease_quantity, name="decrease_quantity"),

    # ==============================
    #          LOGÍSTICA
    # ==============================

    # Lista geral de entregas
    path("dashboard/deliveries/", delivery_list, name="delivery_list"),

    # Detalhe da entrega
    path("dashboard/delivery/<int:pk>/", delivery_detail, name="delivery_detail"),

    # Atualizar status da entrega
    path("dashboard/delivery/<int:pk>/update/", delivery_update, name="delivery_update"),

    # Atribuir entregador
    path("dashboard/delivery/<int:pk>/assign/", assign_delivery_person, name="delivery_assign"),

    # Entregadores
    path("dashboard/delivery-person/", delivery_person_list, name="delivery_person_list"),
    path("dashboard/delivery-person/add/", delivery_person_create, name="delivery_person_add"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
