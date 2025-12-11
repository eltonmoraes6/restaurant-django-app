from django.contrib import admin

from .models import (AboutUs, BookTable, Cart, CMSContent, Delivery,
                     DeliveryPerson, Feedback, ItemList, Items, Order,
                     OrderItem, PageSection)


@admin.register(CMSContent)
class CMSContentAdmin(admin.ModelAdmin):
    list_display = ("page", "key", "updated_at")
    list_filter = ("page",)
    search_fields = ("page", "key", "value")


@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ('page', 'section', 'title', 'updated_at')
    list_filter = ('page',)
    search_fields = ('section', 'content')

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("order_id", "order_user", "status", "updated_at")
    list_filter = ("status", "updated_at")
    search_fields = ("order__id", "order__user__username")

    def order_id(self, obj):
        return obj.order.id

    def order_user(self, obj):
        return obj.order.user.username
    
@admin.register(DeliveryPerson)
class DeliveryPersonAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "phone")

                                             
admin.site.register(ItemList)
admin.site.register(Items)
admin.site.register(AboutUs)
admin.site.register(Feedback)
admin.site.register(BookTable)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)