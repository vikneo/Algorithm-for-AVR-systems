from django import template
from django.http import HttpResponse
from django.core.cache import cache

from ..models import Client

register = template.Library()

@register.inclusion_tag('client/client_main.html')
def client_main() -> dict:
    """
    Вывод всех клиентов на sidebar.
    Кэширование queryset с клиентами.
    """
    try:
        clients = cache.get_or_set('clients', Client.objects.all(), 600)
        return {'clients': clients}
    except Exception as err:
        HttpResponse(f"Клиентов пока нет. Описание ощибки: {err}") # TODO заменитьна логи
