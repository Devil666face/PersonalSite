from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','update_at','category','published')
    list_display_links = ('title',)
    search_fields = ('title','content')
    list_editable = ('published','category')
    list_filter = ('published', 'category','created_at')

class Categorydmin(admin.ModelAdmin):
    # list_display = ('id','title')
    # list_display_links = ('id','title')
    search_fields = ('title',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, Categorydmin)

admin.sites.AdminSite.site_title = 'Управление сайтом'
admin.sites.AdminSite.site_header = 'Управление сайтом'
admin.sites.AdminSite.index_title = 'Главная'