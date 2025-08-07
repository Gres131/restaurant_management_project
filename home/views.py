from django.shortcuts import render
from django.conf import settings
from django.conf import RestaurantInfo

def homepage(request):
    restaurant = RestaurantInfo.objects.first()

    restaurant_name = restaurant.name if restaurant else settings.RESTAURANT_NAME
    restaurant_phone = restaurant.phone if restaurant else settings.RESTAURANT_PHONE

    
    return render(request, 'home/homepage.html', {
        'restaurant_name': restaurant_name,
        'restaurant_phone': restaurant_phone
        })
