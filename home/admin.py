from django.contrib import admin
from .models import RestaurantInfo, RestaurantLocation
from .models import MenuItem
# Register your models here.
admin.site.register(RestaurantInfo)
admin.site.register(RestaurantLocation)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_diaplay = ("name", "price")
