from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from .models  import RestaurantInfo, RestaurantLocation, MenuItem, MenuCategory
from products.models import Menu
from .forms import ContactForm
import logging, requests


from rest_framework.generics import ListAPIView
from .serializers import MenuCategorySerializer

logger = logging.getLogger(__name__)

def homepage(request):
    """Render the homepage with restaurant info, menu, and search."""
    restaurant_display_name = getattr(settings, 'RESTAURANT_NAME', 'Our Restaurant')
    restaurant_display_phone = getattr(settings, 'RESTAURANT_PHONE', '000-000-0000')
    restaurant_info = RestaurantInfo.objects.first()
    restaurant_location = RestaurantLocation.objects.first()
    opening_hours = "Mon-Fri: 11am-9pm, Sat-Sun: 10am-10pm"

    
    # get query param
    search_query = request.GET.get("q", "")

    # filter menu items by name (fixed variable name)
    if search_query:
        menu_items = MenuItem.objects.filter(name_icontains=query)
    else:
        menu_items = MenuItem.objects.all()
    

    # Cart count from session
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())
        
    
    context = {
        "restaurant_info": restaurant_info,
        "restaurant_name": restaurant_info.name if restaurant_info else "Our Restaurant",    
        "restaurant_phone": restaurant_info.phone if rest  else "000-000-000",
        "opening_hours": opening_hours,
        "menu_items": menu_items, 
        "search_query": search_query,
        "restaurant_location": restaurant_location,
        "cart_count": cart_count, 
           
    }
    
    return render(request, template_name='home/homepage.html', context=context)


def add_to_cart(request, item_id):
    """Add item to shopping cart (stored in session)"""
    item = get_object_or_404(MenuItem, id=item_id)
    cart = request.session.get('cart', {})

    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session['cart'] = cart

    return redirect("homepage")
      
def contact_us (request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact=form.save()

            # Send email notification
            subject = f"New Contact Form Submission from {contact.name}"
            message = f"Message from {contact.name} ({contact.email}):\n\n{contact.message}"
            from_email = setting.DEFAULT_FROM_EMAIL
            recipient_list = [settings.RESTAURANT_EMAIL]

            send_mail(subject, message, from_email, recipient_list) 
            return redirect("contact_us")
    else:
        form = ContactForm()


    return render(request, template_name="home/contact_us.html", {"form":form})

def faq_view(request):
    """Render FAQ Page"""
    return render(request, template_name="home/faq.html")

class MenuCategoryListView(ListAPIView):
    """
    API endpoint to retrieve all menu categories.
    Allows frontend to fetch categories dynamically.
    """
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer