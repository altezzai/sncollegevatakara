from django import template

from myapp.models import CampusLifePage

register = template.Library()


@register.simple_tag
def campus_life_nav_pages():
    return CampusLifePage.objects.filter(is_published=True)
