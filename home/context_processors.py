from django.conf import settings
from django.utils.timezone import now

def footer_context(request):
    return {
        "restaurant_name": getattr(settings, "RESTAURANT_NAME, "Default Restaurant"),
        "restaurant_phone": getattr(settings, "RESTAURANT_PHONE", "N/A"),
        "restaurant_address": getattr(settings, "RESTAURANT_ADDDRESS", ""),
        "restaurant_email": getattr(settings, "RESTAURANT_EMAIL", ""),
        "current_year": now().year,
    }