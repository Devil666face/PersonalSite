from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category
from .forms import ArtcileForm

#Class view paradigm
from django.views.generic import ListView, DetailView, CreateView

from django.urls import reverse_lazy

class HomeArticle(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'articles'
    # extra_context = {
    #     'title':'Главная'
    # }

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['title_current'] = 'Главная'
        return context

    def get_queryset(self):
        return Article.objects.filter(published=True).select_related('category')

# def home_page(request):
#     # Articles = Article.objects.order_by('-created_at')
#     articles = Article.objects.all()
#     context = {
#         'articles': articles,
#         'title': 'Все посты',
#     }
#     return render(request, template_name='blog/home.html', context=context)

class ArticleByCategory(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'articles'
    # allow_empty = False #Запрещаем показ пустых списков

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(pk=self.kwargs['category_id'])
        context['title'] = category
        context['title_current'] = category
        context['category'] = category
        return context
    
    def get_queryset(self):
        return Article.objects.filter(category_id = self.kwargs['category_id'], published=True).select_related('category')

# def get_category(request, category_id):
#     articles = Article.objects.filter(category_id = category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'articles': articles,
#         'category': category,
#     }
#     return render(request,template_name='blog/home.html', context=context)

class ViewArticle(DetailView):
    model = Article
    # template_name = 'blog/article_detail.html'
    # pk_url_kwarg = 'article_id'
    context_object_name = 'article_item'
    
    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# def  view_article(request, article_id):
#     # article_item = Article.objects.get(pk=article_id)
#     article_item = get_object_or_404(Article, pk=article_id)
#     context = {
#         'article_item': article_item,
#     }
#     return render(request,template_name='blog/article.html',context=context)

class CreateArticle(CreateView):
    form_class = ArtcileForm #Имя класса формы
    template_name = 'blog/add_article.html'
    # success_url = reverse_lazy('home')

# def add_article(request):
#     if request.method == 'POST':
#         article_add_form = ArtcileForm(request.POST)
#         if article_add_form.is_valid():
#             # Для ручного способа создания формы
#             # added_article = Article.objects.create(**article_add_form.cleaned_data)
#             # Для автоматического через джанго
#             added_article = article_add_form.save()
#             return redirect(added_article)
#     else:
#         article_add_form = ArtcileForm()
#     return render(request, 'blog/add_artcile.html', {'article_add_form': article_add_form})
