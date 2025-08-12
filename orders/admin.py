from django.contrib import admin #  Added missing import
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','status', 'total_amount', 'created_at')
    list_filter = ('status','created_at')
    search_fields = ('customer_username', 'customer_email')#Corrected filed names
    ordering = ('-created_at',)


    #Only keep if `order_item` is actually a ManyToManyField in Order model
    filter_horizontal = ('order_items',)



admin.site.register(Order, OrderAdmin)
