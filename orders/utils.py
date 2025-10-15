import string 
import secrets
from .models import Coupon

def generate_copon_code(length=10):
    """
    Generate a unique alphanumeric coupon code.

    Args:
        length (int): The desired length of the coupon code (default: 10)
    
    Returns:
        str: Aunique alphanumeric coupon code.
    """
    characters = string.ascii_uppercase + string.digits

    while True:
        #Generate a random coupon code
        code = ''.join(secrets.choice(characters) for _ in range(length))

        # Ensure the code is unique in the database
        if not Coupon.objects.filter(code=code).exists():
            return code