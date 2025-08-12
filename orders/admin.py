from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','status', 'total_amount', 'created_at')
    list_filter = ('status','created_at')
    search_fields = ('customer_username', 'customer_email')
    ordering = ('-created_at',)
    filter_horizontal = ('order_items',)



admin.site.register(Order, OrderAdmin)
