from dataclasses import fields
import re
from tabnanny import verbose
from django import forms
from .models import Category, Article
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs = {"class":"form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs = {"class":"form-control"}))
    

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text="Имя пользователя должно быть уникальным", widget=forms.TextInput(attrs = {"class":"form-control"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs = {"class":"form-control"}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs = {"class":"form-control"}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs = {"class":"form-control"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs = {"class":"form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs = {"class":"form-control"}))
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')


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
