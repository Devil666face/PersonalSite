from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category
from .forms import ArtcileForm, UserRegisterForm, UserLoginForm
# Login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
#Class view paradigm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
# Paginator
from django.core.paginator import Paginator
from django.contrib import messages
# mixin
# from .utils import Mixin
# register and login

# def get_paginating(request):
    # articles = Article.objects.all()
    # paginator = Paginator(articles, 3)
    # page_num = request.GET.get('page', 1)
    # page_obj = paginator.get_page(page_num)
    # 

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,'Пользователь создан.')
            return redirect('home')
        else:
            messages.error(request,f'Ошибка регистрации.')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {"form":form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, 'blog/login.html', {"form":form})

def user_logout(request):
    logout(request)
    return redirect('login')

class HomeArticle(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'articles'
    paginate_by = 5
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
    paginate_by = 5
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

class CreateArticle(LoginRequiredMixin, CreateView):
    form_class = ArtcileForm #Имя класса формы
    template_name = 'blog/add_article.html'
    login_url = '/login/'
    # raise_exception = True Ошибка если пользователь не авторизован
    # login_url = reverse_lazy('home')
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

