from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category
from .forms import ArtcileForm

# Create your views here.

def home_page(request):
    # Articles = Article.objects.order_by('-created_at')
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'title': 'Все посты',
    }
    return render(request, template_name='blog/home.html', context=context)

def get_category(request, category_id):
    articles = Article.objects.filter(category_id = category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'articles': articles,
        'category': category,
    }
    return render(request,template_name='blog/home.html', context=context)

def  view_article(request, article_id):
    # article_item = Article.objects.get(pk=article_id)
    article_item = get_object_or_404(Article, pk=article_id)
    context = {
        'article_item': article_item,
    }
    return render(request,template_name='blog/article.html',context=context)

def add_article(request):
    if request.method == 'POST':
        article_add_form = ArtcileForm(request.POST)
        if article_add_form.is_valid():
            # Для ручного способа создания формы
            # added_article = Article.objects.create(**article_add_form.cleaned_data)
            # Для автоматического через джанго
            added_article = article_add_form.save()
            return redirect(added_article)
    else:
        article_add_form = ArtcileForm()
    return render(request, 'blog/add_artcile.html', {'article_add_form': article_add_form})
