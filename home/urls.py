from django.urls import path
from .views import *
from home.views import homepage
from django.conf.urls import handler404

handler404 = 'home.views.custom_404_view'

urlpatterns = [ path('', homepage, name='homepage'), path('admin/', admin.site.urls), path('menu/', views.menu_list, name='menu_list'), path('contact/', views.contact_us, name='contact_us')]
