from django.contrib import admin

from .models import (AboutUs, BookTable, Cart, CMSContent, Feedback, ItemList,
                     Items, Order, OrderItem, PageSection)


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

                                             
admin.site.register(ItemList)
admin.site.register(Items)
admin.site.register(AboutUs)
admin.site.register(Feedback)
admin.site.register(BookTable)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)