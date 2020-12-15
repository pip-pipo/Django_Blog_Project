
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import widgets
from django.utils.translation import gettext, gettext_lazy as _
from .models import PostData


class SignupFrom(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control my-1'}))
    password2 = forms.CharField(
        label='Confirm_password(again)', widget=forms.PasswordInput(attrs={'class': 'form-control my-1'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name', 'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control my-1'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control my-1'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control my-1'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control my-1'}),
                   }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'autofocus': True}))
    password = forms.CharField(label=_("password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class PostFrom(forms.ModelForm):
    class Meta:
        model = PostData
        fields = ['titel', 'desc']
        labels = {'titel': 'Titel', 'desc': 'Description'}
        widgets = {'titel': forms.TextInput(attrs={'class': 'form-control'}),
                   'desc': forms.Textarea(attrs={'class': 'form-control'}),
                   }
