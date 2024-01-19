from django.contrib import admin
from django.contrib.auth.models import User

from users.models import Profile


@admin.action(description='В архив')
def mark_archived(modeladmin, request, queryset) -> None:
    """
    Действи для добавления статуса пользователю "В архиве".
    """
    queryset.update(archived=True)


@admin.action(description='Снять архивацию')
def remove_archived(modeladmin, request, queryset) -> None:
    """
    Действие для снятия с пользователя статуса "В архиве".
    """
    queryset.update(archived=False)


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    """
    Регистрация моделли "Profile"
    """
    actions = [
        mark_archived,
        remove_archived
    ]
    list_display = ['get_username', 'get_firstname', 'get_last_name', 'phone', 'get_email', 'archived']
    search_fields = ['phone', 'get_email']
    fieldsets = [
        (None, {
            'fields': ('user', 'phone'),
        }),
        ('Extra option', {
            'fields': ('archived',),
            'classes': ('collapse',)
        })
    ]

    def get_username(self, obj: Profile):
        """ Возвращает Login пользователя """
        return obj.user.username

    def get_firstname(self, obj: Profile):
        """ Возвращает Имя пользователя """
        return obj.user.first_name
    
    def get_last_name(self, obj: Profile) -> str:
        """ Возвращает Фамилию пользователя """
        return obj.user.last_name
    
    def get_email(self, obj: Profile):
        """ Возвращает почту пользователя """
        return obj.user.email
    
    get_username.short_description = 'Логин'
    get_firstname.short_description = 'Имя'
    get_last_name.short_description = 'Фамилия'
    get_email.short_description = 'Почта'
