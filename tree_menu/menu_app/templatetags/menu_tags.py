from django import template
from django.shortcuts import get_object_or_404
from menu_app.models import MenuItem


register = template.Library()


@register.simple_tag
def draw_menu(menu_name, current_url):
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    current_menu_item = get_object_or_404(MenuItem, name=menu_name)
    parents = []
    while current_menu_item.parent is not None:
        parents.append(current_menu_item.parent)
        current_menu_item = current_menu_item.parent

    context = {'menu_items': menu_items, 'parents': parents}

    return context
