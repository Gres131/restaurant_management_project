from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RestaurantInfo(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=225, blank=True)


    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    bio =models.TextField(blank=True)


    def __str__(self):
        return f"{self.user.username} Profile"