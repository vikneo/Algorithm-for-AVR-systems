from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)


class RegisterUserForm(UserCreationForm):
    """
    User register form
    """
    email = forms.CharField(
        label='Почта',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Ваш email',
            },
        ),
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
            'class': 'form-input',
            'placeholder': 'Введите пароль',
            },
        ),
    )
    password2 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
            'class': 'form-input',
            'placeholder': 'Повторите пароль',
            },
        ),
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']



class UserFormAuth(AuthenticationForm):
    """
    User authentication form
    """
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Логин/Email',
            },
        ),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Введите пароль',
            },
        ),
    )

    class Meta:
        model = User
        fields = ["username", "password"]