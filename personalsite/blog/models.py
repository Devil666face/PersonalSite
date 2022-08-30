from django.db import models
from django.urls import reverse

class Article(models.Model):
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article',kwargs={"pk": self.pk})
        # return reverse('article',args=str(self.pk))

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']

    title = models.CharField(max_length=255, db_index=True, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, verbose_name='Фото')
    file = models.FileField(upload_to='files/%Y/%m/%d/',blank=True, verbose_name='Прикрепленный файл')
    published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория', related_name='get_articles')

class Category(models.Model):
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category',kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    title = models.CharField(max_length=255, db_index=True,verbose_name='Название категории')
