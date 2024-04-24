from django.urls import path

from .views import (
    RegisterUserView,
    LoginUserView,
    LogOutUserView,
    )


app_name = 'profile'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogOutUserView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
]