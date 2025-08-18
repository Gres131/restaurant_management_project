from django.contrib import admin
from .models import Item


# Custom Admins
# class MenuAdmin(admin.ModelAdmin):
#    list_display = ('name', 'price','category', 'available')
#    list_filter = ('category', 'available')
#    search_fields = ('name', 'description')
#    ordering = ('name',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name','item_price', 'created_at')
    search_field = ('item_name',)
    ordering = ('item_name',)

# Register your models here.
# admin.site.register(Menu, MenuAdmin)
admin.site.register(Item,ItemAdmin)