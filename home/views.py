from django.shortcuts import render
from django.conf import settings

def homepage(request):
    restaurant_name = settings.RESTAURANT_NAME
    return render(request, 'home/homepage.html', {'restaurant_name': restaurant_name})
