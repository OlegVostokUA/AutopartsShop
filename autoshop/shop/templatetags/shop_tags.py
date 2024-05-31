from django import template
from django.utils.safestring import mark_safe
from ..models import Component

register = template.Library()


@register.simple_tag
def total_components():
    return Component.objects.count()
