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

    if restaurant:

        restaurant_display_name = f"{restaurant.name}" 
        restaurant_display_phone = f"{restaurant.phone}" 
    else:
        restaurant_display_name = f"{default_restaurant_name}"
        restaurant_display_phone = f"{default_restaurant_phone}"


    opening_hours = "Mon-Fri: 11am-9pm, Sat-Sun: 10am-10pm"

    
     context = {
        "restaurant_name": restaurant_display_name,
        "restaurant_phone": restaurant_display_phone,
        "opening_hours": opening_hours     
    }
    
    return render(request, 'home/homepage.html', context)
   
