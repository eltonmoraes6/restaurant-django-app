from django.contrib import admin

from .models import (AboutUs, BookTable, Cart, Feedback, ItemList, Items,
                     Order, OrderItem)

admin.site.register(ItemList)
admin.site.register(Items)
admin.site.register(AboutUs)
admin.site.register(Feedback)
admin.site.register(BookTable)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)