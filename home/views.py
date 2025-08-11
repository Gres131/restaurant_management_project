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

    default_restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'Our Restaurant')
    default_restaurant_phone = getattr(settings, 'RESTAURANT_PHONE', '000-000-0000')


    restaurant_name = restaurant.name if restaurant else settings.RESTAURANT_NAME
    restaurant_phone = restaurant.phone if restaurant else settings.RESTAURANT_PHONE
    
     context = {
        'restaurant_name': restaurant_name,
        'restaurant_phone': restaurant_phone
     }
    
    return render(request, 'home/homepage.html', context)
   
