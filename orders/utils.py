import string 
import secrets
from .models import Coupon

def generate_copon_code(length=10):
    """
    Generate a unique alphanumeric coupon code and save it to the database.

    Arge:
        length (int) Length of the coupon code. Default is  10.
        discount_percent (int): Discount percentage. Default is 10%.

    Returns:
        Coupon: The newly created Coupon instance.
    """
    characters = string.ascii_uppercase + string.digits

    while True:
       
        code = ''.join(secrets.choice(characters) for _ in range(length))
        if not Coupon.objects.filter(code=code).exists(): 
            # Create and save the unique coupon
            coupon = Coupon.objects.create(code=code, discount_percent=discount_percent)
            return coupon