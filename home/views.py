from django.shortcuts import render
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def homepage(request):
    try:
        restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'Our Restaurant')


        context = {
            "restaurant_name": settings.RESTAURANT_NAME
        }
        return render(request, 'home/homepage.html', context)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def contact_us(request):
    return render(request, 'home/contact_us.html')
