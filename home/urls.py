from django.urls import path
from django.contrib import admin
from . import views
from .views import(
    homepage,
    feedback_view,
    menu_view,
    MenuCategoryListView,
)

# Custom 404 handler
handler404 = 'home.views.custom_404_view'

urlpatterns = [ 
    path('', homepage, name='homepage'), 
    path('admin/', admin.site.urls), 
    path("menu/", views.menu_list, name="menu_list"), 
    path("contact/", views.contact_us, name="contact_us"),  
    path("reservations/", views.reservations, name="reservations"),
    path('feedback/', views.feedback, name='feedback')
    path('api/menu/', menu_view, name='menu_api'),
    path("locations/", views.restaurant_locations, name="restaurant_locations"),
    path("about/", views.about,name="about"),
    path("add-to-cart/<int:item_id>/", views.add_to_cart, name="add_to_cart"),
    path('api/categories/', MenuCategoryListView.as_view(), name='menu-category-list'),
]
