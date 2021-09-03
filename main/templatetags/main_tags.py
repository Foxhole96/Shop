from django import template
from main.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def category_slider_home():
    return Category.objects.order_by('-id')[:5]


@register.simple_tag()
def menu():
    return Category.objects.all()


@register.simple_tag()
def feature_categories():
    return Category.objects.order_by('id')[:4]


@register.simple_tag()
def page_data():
    return SinglePages.objects.all().order_by('id')
