from django import template 

register = template.library()

@register.filter
def custom_datetime(value):
    if not value:
        return ""
    return value.strftime("%A, %d %B %Y at %I:%M %p")