from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','update_at','category','published', 'get_photo')
    list_display_links = ('title',)
    search_fields = ('title','content')
    list_editable = ('published','category')
    list_filter = ('published', 'category','created_at')
    fields = ('title','photo','get_photo','content','created_at','update_at','category','published')
    readonly_fields = ('get_photo','created_at','update_at')
    # fieldsets есть такой метод для большей кастомизации
    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="150">') if obj.photo else '❌'

    get_photo.short_description = 'Фото'
            


class Categorydmin(admin.ModelAdmin):
    # list_display = ('id','title')
    # list_display_links = ('id','title')
    search_fields = ('title',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, Categorydmin)

admin.sites.AdminSite.site_title = 'Управление сайтом'
admin.sites.AdminSite.site_header = 'Управление сайтом'
admin.sites.AdminSite.index_title = 'Главная'