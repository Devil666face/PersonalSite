from django import template
from blog.models import Category

register = template.Library()

@register.simple_tag(name = 'get_categories')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('blog/list_categories.html')
def show_categories(category):
    categories = Category.objects.all()
    return {'categories':categories,'category':category}