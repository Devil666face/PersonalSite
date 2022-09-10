from django import template
from blog.models import Category
from django.db.models import Count

register = template.Library()

@register.simple_tag(name = 'get_categories')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('blog/list_categories.html')
def show_categories(category):
    # Убираем категории без статей
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('get_articles')).filter(cnt__gt=0)
    return {'categories':categories,'category':category}