from django.dispatch import receiver
from django.db.models.signals import pre_save

from utils.slugify import slugify

from .models import (
    Client,
    Subjects,
    Product,
    SmartRelay,
    ProcessedImageField,
)

@receiver(pre_save, Client)
@receiver(pre_save, Subjects)
@receiver(pre_save, SmartRelay)
def get_slugify(instance, **kwargs) -> None:
    """
    Перед сохранением созданной записи в БД проверяется поле "slug",
    если поле с пустым значчение, то метод "get_slug" заполняет поле
    """
    if not instance.slug:
        instance.slug = slugify(instance.name)

