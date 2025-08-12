from django.shortcuts import render
from django.conf import settings
from django.utils.timezone import now

def homepage(request):
    context = {
    "restaurant_name": settings.RESTAURANT_NAME
    }
    return render(request, 'home/homepage.html', context)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def contact_us(request):
    return render(request, 'home/contact_us.html')

def reservations(request):
    return render(request, 'home/reservations.html')
