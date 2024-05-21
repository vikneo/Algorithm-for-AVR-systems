from django.dispatch import receiver
from django.db.models.signals import pre_save

from utils.slugify import slugify

from .models import (
    Client,
    Subjects,
    Product,
    SmartRelay,
    ProductImage,
)

@receiver(pre_save, sender=Client)
@receiver(pre_save, sender=Subjects)
@receiver(pre_save, sender=SmartRelay)
def get_slugify_save(sender, instance, **kwargs) -> None:
    """
    Перед сохранением созданной записи в БД проверяется поле "slug",
    если поле с пустым значчение, то метод "get_slug_save" заполняет поле
    """
    if not instance.slug:
        instance.slug = slugify(instance.name)


@receiver(pre_save, sender=Product)
def get_slugify_product_save(sender, instance, **kwargs) -> None:
    """
    Перед сохранением созданной записи в БД проверяется поле "slug",
    если поле с пустым значчение, то метод "get_slug_save" заполняет поле
    """
    if not instance.slug:
        name_slug = f'{instance.subject.name}_{instance.name}_{instance.id_product}'
        instance.slug = slugify(name_slug)


@receiver(pre_save, sender=Subjects)
def get_photo_save(sender, instance, **kwargs) -> None:
    """
    Перед сохранением записи модели "Subjects", проверяется поле "photo",
    если поле пустое, метод "get_photo_save" добавляет изображение по умоолчанию
    """
    if not instance.photo:
        instance.photo = '../media/default.PNG'
