from django import template
from django.conf import settings

register = template.Library()

@register.filter
def adjust_for_counter(value, page):
    value = int(value)
    page = int(page)
    # Ensure that you use the correct pagination settings or adjust if needed
    return settings.RESULTS_PER_PAGE * (page - 1) + value
