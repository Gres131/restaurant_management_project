from django.contrib import admin
from .models import RestaurantInfo, RestaurantLocation

# Register your models here.
admin.site.register(RestaurantInfo)
admin.site.register(RestaurantLocation)
