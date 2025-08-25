from django.shortcuts import render
from django.conf import settings
from .models  import RestaurantInfo
from .models import RestaurantLocation
from .forms import Contactform
import logging 
import requests


logger = logging.getLogger(__name__)

def homepage(request):
    restaurant_display_name = getattr(settings, 'RESTAURANT_NAME', 'Our Restaurant')
    restaurant_display_phone = getattr(settings, 'RESTAURANT_PHONE', '000-000-0000')


    opening_hours = "Mon-Fri: 11am-9pm, Sat-Sun: 10am-10pm"


    menu_items = []
    api_url = "http://localhost:8000/api/menu/"
    try:
        response =requests.get(api_url, timeout=5)
        if response.status_code ==  200:
            menu_items = response.json()
    except requests.exceptions.RequestEception as e:
        logger.error(f"Error fetching menu data: {e}")
        
    
     context = {
        "restaurant_name": restaurant_display_name,
        "restaurant_phone": restaurant_display_phone,
        "opening_hours": opening_hours,
        "menu_items": menu_items     
    }
    
    return render(request, 'home/homepage.html', context)


 def restaurant_locations(request):
    location = RestaurantLocation.objects.all()
    return render(request, "home/restaurant_locations.html", {"locations": location})
      
