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
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        db_table = 'profiles'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'


class Role(models.Model):
    """
    Класс описывает роль сотрудника компании
    """
    class StatusRole(models.TextChoices):
        """
        Набор ролей для сотрудников
        """
        CRC = ('Схемотехник', 'Схемотехник')
        DSG = ('Конструктор', 'Конструктор')
        PRM = ('Программист', 'Программист')
        SLR = ('Отсутствует', 'Отсутствует')

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Профиль', related_name='roles')
    role = models.CharField(max_length=15, verbose_name='Роль', choices=StatusRole, blank=True, default=StatusRole.SLR)

    class Meta:
        db_table = 'roles'
        verbose_name = 'роль'
        verbose_name_plural = 'роли'
