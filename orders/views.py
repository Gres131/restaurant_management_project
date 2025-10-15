from django.shortcuts import render
from orders.utils import generate_coupon_code
from orders.models import generate_coupon_code

def create_new_coupon():
    code = generate_coupon_code(12)
    Coupon.objects.create(code=code, discount_percent=15)
    print("New coupon created:", code)
