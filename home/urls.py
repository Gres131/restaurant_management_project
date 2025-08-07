from django.urls import path
from .views import *
from home.views import homepage

urlpatterns = [ path('', homepage, name='homepage'), path('admin/', admin.site.urls)]