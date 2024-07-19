from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 border border-gray-300 rounded-lg focus:outline-none focus:border-gray-400 focus:ring-0',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 border border-gray-300 rounded-lg focus:outline-none focus:border-gray-400 focus:ring-0',
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 border border-gray-300 rounded-lg focus:outline-none focus:border-gray-400 focus:ring-0',
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Your email',
        'class': 'w-full py-4 px-6 border border-gray-300 rounded-lg focus:outline-none focus:border-gray-400 focus:ring-0',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 border border-gray-300 rounded-lg focus:outline-none focus:border-gray-400 focus:ring-0',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm your password',
        'class': 'w-full py-4 px-6 border border-gray-300 rounded-lg focus:outline-none focus:border-gray-400 focus:ring-0',
    }))