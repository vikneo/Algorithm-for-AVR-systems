from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Класс описывает модель пользователя
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone = models.CharField(max_length=20, verbose_name='Телефон', unique=True)
    archived = models.BooleanField(default=False, verbose_name='Архивация')

    def __str__(self) -> str:
        return f'{self.user}'

    class Meta:
        db_table = 'profiles'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
