from django.shortcuts import render
from django.conf import settings

def homepage(request):
    restaurant = RestaurantInfo.objects.first()
    return render(request, 'home/homepage.html', {
        'restaurant_name': restaurant_name,
        'restaurant_phone': restaurant_phone
        })
