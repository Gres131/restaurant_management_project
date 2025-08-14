from django.urls import path
from .views import ItemView
from .views import menu_list

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path ('menu/', menu_list, name='menu-list'),
]


