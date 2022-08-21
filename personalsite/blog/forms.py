from django import forms
from .models import Category, Article
from django.core.exceptions import ValidationError
import re

# Создаваемая в ручную форма
# class ArtcileForm(forms.Form):
    # title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs = {"class":"form-control"}))
    # content = forms.CharField(label='Контент', required=False, widget=forms.Textarea(attrs = {
    #     "class":"form-control",
    #     "rows":5,
    # }))
    # published = forms.BooleanField(label='Опубликовано',required=False, initial=True)
    # category = forms.ModelChoiceField(empty_label=None, label='Категория',queryset=Category.objects.all(), widget=forms.Select(attrs = {
    #     "class":"form-control",
    # }))

# Автоматическая форма от джанго
class ArtcileForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = '__all__'
        fields = ['title','content','category','photo','file','published']
        widgets = {
            'title':forms.TextInput(attrs = {"class":"form-control"}),
            'content':forms.Textarea(attrs = {"class":"form-control","rows":5}),
            'category':forms.Select(attrs = {"class":"form-control"}),
            'photo':forms.FileInput(attrs = {"class":"form-control"}),
            'file':forms.FileInput(attrs = {"class":"form-control"}),
            'published':forms.CheckboxInput(attrs = {"class":"form-check"}),
            
        }

    # Валидация поля title
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match('\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title