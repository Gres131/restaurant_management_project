from django.shortcuts import render, redirect
from django.conf import settings
from .models  import RestaurantInfo, RestaurantLocation,
from products.models import Menu
from .forms import ContactForm
# import logging, requests


logger = logging.getLogger(__name__)

def homepage(request):
    restaurant_display_name = getattr(settings, 'RESTAURANT_NAME', 'Our Restaurant')
    restaurant_display_phone = getattr(settings, 'RESTAURANT_PHONE', '000-000-0000')
    restaurant_info = RestaurantInfo.objects.first()

    opening_hours = "Mon-Fri: 11am-9pm, Sat-Sun: 10am-10pm"

    
    # get query param
    query request.GET.get("q", "")

    # correct filter syntax (double underscore)
    if query:
        menu_items = MenuItem.objects.filter(name_icontains=query)
    else:
        menu_items = MenuItem.objects.all()

        # fetch first restaurant location
    restaurant_location = RestaurantLocation.objects.first()


    # api_url = "http://localhost:8000/api/menu/"
    # try:
    #     response =requests.get(api_url, timeout=5)
    #     if response.status_code ==  200:
    #         menu_items = response.json()
    # except requests.exceptions.RequestEception as e:
    #     logger.error(f"Error fetching menu data: {e}")
        
    
     context = {
        "restaurant_name": restaurant_display_name,
        "restaurant_phone": restaurant_display_phone,
        "opening_hours": opening_hours,
        "menu_items": menu_items, 
        "query": query,
        "restaurant_location": restaurant_location,    
    }
    
    return render(request, 'home/homepage.html', context)


#  def restaurant_locations(request):
#     location = RestaurantLocation.objects.all()
#     return render(request, "home/restaurant_locations.html", {"locations": location})
      
# def contact_us (request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             returnredirect("contact_us")
#     else:
#         form = ContactForm()
#         return render(request, "home/contact_us.html", {"form":form})