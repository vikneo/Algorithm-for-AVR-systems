from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Profile, Role
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
    
    def get_username(self, form):
        username = form.cleaned_data.get('email')
        return username
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()
        user.username = self.get_username(form)
        user.email = form.cleaned_data.get('email')
        user.save()

        profile = Profile.objects.create(
            user=user,
        )
        Role.objects.create(
            profile=profile,
        )

        login(self.request, user)

        return redirect(reverse_lazy('product:clients'))


class LoginUserView(LoginView):
    """
    Login iin the system
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
    next_page = reverse_lazy('product:clients')