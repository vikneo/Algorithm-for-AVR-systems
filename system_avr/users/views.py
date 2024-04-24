from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Profile
from .forms import RegisterUserForm, UserFormAuth


class RegisterUserView(CreateView):
    """
    The registration form
    """
    template_name = 'profile/register.html'
    form_class = RegisterUserForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title='Регистрация'
        )
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        Profile.objects.create(
            user=user,
        )

        user_auth = authenticate(username=username, password=password)
        login(self.request, user_auth)

        return redirect(reverse_lazy('product:subject'))


class LoginUserView(LoginView):
    """
    
    """
    form_class = UserFormAuth
    template_name = 'profile/login.html'
    success_url = reverse_lazy('product:subject')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title='Авторизация',
        )
        return context


class LogOutUserView(LogoutView):
    """
    Log Out of the system
    """
    next_page = reverse_lazy('profile:login')