from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']