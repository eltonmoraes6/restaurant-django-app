from django.contrib.auth.models import User
from django.db import models


class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)

    def __str__(self):
        return self.Category_name


class Items(models.Model):
    Item_name = models.CharField(max_length=40)
    description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.Item_name


class AboutUs(models.Model):
    Description = models.TextField(blank=False)


class Feedback(models.Model):
    User_name = models.CharField(max_length=15)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField()
    Image = models.ImageField(upload_to='feedback/', blank=True)

    def __str__(self):
        return self.User_name


class BookTable(models.Model):
    Name = models.CharField(max_length=15)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()

    def __str__(self):
        return self.Name


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)
    item = models.ForeignKey(Items, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.item.Item_name}"


# ------------------------
#  NEW ORDER MODELS
# ------------------------

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Items, on_delete=models.CASCADE)  # refer directly (no import)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_total(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.item.Item_name} ({self.quantity})"

class CMSContent(models.Model):
    page = models.CharField(max_length=50)      # ex: home, about, footer
    key = models.CharField(max_length=50)       # ex: hero_title, about_text
    value = models.TextField()                  # editable text
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('page', 'key')

    def __str__(self):
        return f"{self.page} - {self.key}"

class PageSection(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home Page'),
        ('about', 'About Page'),
        ('menu', 'Menu Page'),
        ('footer', 'Footer'),
        ('contact', 'Contact Info'),
    ]

    page = models.CharField(max_length=50, choices=PAGE_CHOICES)
    section = models.CharField(max_length=100)  # example: 'hero_title'
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="cms/", blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('page', 'section')

    def __str__(self):
        return f"{self.page} - {self.section}"

class Delivery(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pendente"),
        ("preparing", "Em Separação"),
        ("shipping", "Em Rota"),
        ("delivered", "Entregue"),
        ("cancelled", "Cancelado"),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="delivery")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    updated_at = models.DateTimeField(auto_now=True)

    # FIX AQUI
    delivery_person = models.ForeignKey(
        "DeliveryPerson",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="deliveries"
    )

    tracking_note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Entrega Pedido #{self.order.id}"


class DeliveryPerson(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
