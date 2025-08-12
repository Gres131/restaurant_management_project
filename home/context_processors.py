from django.conf import settings
from django.utils.timezone import now

def footer_context(request):
    return {
        "restaurant_name": getattr(settings, "RESTAURANT_NAME, "Default Restaurant"),
        "current_year": now().year
    }