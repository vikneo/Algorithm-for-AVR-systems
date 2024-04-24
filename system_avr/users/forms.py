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
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Поле для ввода',
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
        fields = ['username', 'password1', 'password2']



class UserFormAuth(AuthenticationForm):
    """
    User authentication form
    """
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Введите ваш логин',
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