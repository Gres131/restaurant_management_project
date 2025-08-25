from django.urls import path
from .views import *
from home.views import homepage
from django.conf.urls import handler404
from . import views
from .views import feedback_view
from .views import menu_view

handler404 = 'home.views.custom_404_view'

urlpatterns = [ path('', homepage, name='homepage'), 
path('admin/', admin.site.urls), 
path('menu/', views.menu_list, name='menu_list'), 
path('contact/', views.contact_us, name='contact_us'), 
path("", views.homepage, name = "homepage"), 
path('reservations/', views.reservations, name='reservations'),
path('feedback/', views.feedback, name='feedback')
path('api/menu/', menu_view, name='menu_api'),
path("locations/", views.restaurant_locations, name="restaurant_locations"),
]
