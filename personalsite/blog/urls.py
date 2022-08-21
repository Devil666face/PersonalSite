from django.urls import path
from .views import *

urlpatterns = [
    # path('',home_page, name='home'),
    path('', HomeArticle.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', ArticleByCategory.as_view(), name='category'),
    # path('article/<int:article_id>/', view_article, name='article'),
    path('article/<int:pk>/', ViewArticle.as_view(), name='article'),

    path('article/add-article/', add_article, name='add_artcile'),
]