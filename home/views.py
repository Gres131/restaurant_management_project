from django.shortcuts import render
from django.conf import settings
from .models  import RestaurantInfo
import logging 

logger = logging.getLogger(__name__)

def homepage(request):
    try:
        restaurant = RestaurantInfo.objects.first()
    except Exception as e:
        logger.error(f"Database error fetching restaurant info: {e}")
        restaurant = None


    restaurant_name = restaurant.name if restaurant else settings.RESTAURANT_NAME
    restaurant_phone = restaurant.phone if restaurant else settings.RESTAURANT_PHONE

    
    return render(request, 'home/homepage.html', {
        'restaurant_name': restaurant_name,
        'restaurant_phone': restaurant_phone
        })
