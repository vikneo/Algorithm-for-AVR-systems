from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


def product_images_directory_path(instance: 'Image', filename: str) -> str:
    """
    Функция генерирует путь сохранения изображений с привязкой к id товара

    :param instance: объект Image
    :param filename: имя файла
    :return: str - путь для сохранения
    """

    return f'products/product_{instance.product_id}/{filename}'


class Client(models.Model):
    """
    Класс описывает модель клиента
    """
    name = models.CharField(max_length=100, verbose_name='Клиент')
    slug = models.SlugField(max_length=100, verbose_name='URL')

    class Meta:
        db_table = 'clients'
        verbose_name = 'client'
        verbose_name_plural = 'clients'


class SmartRelay(models.Model):
    """
    Класс описывает модель логических контроллеров
    """
    class TypeRelay(models.IntegerChoices):
        PR200 = 1, 'ПР200'
        PR205 = 2, 'ПР205'
        PR103 = 3, 'ПР103'
        SR3B261BD = 4, 'SR3B261BD'
        SR2B201FU = 5, 'SR2B201FU'
        SR2B121FU = 6, 'SR2B121FU'
        ONI = 7, 'Oni'


    brend = models.CharField(max_length=100, verbose_name='Бренд')
    slug = models.SlugField(max_length=100, verbose_name='URL')
    name = models.IntegerField(choices=TypeRelay.choices, verbose_name='Модель')
    
    class Meta:
        db_table = 'smartrelay'
        verbose_name = 'relay'
        verbose_name_plural = 'relays'


class Product(models.Model):
    """
    Класс описывает модель продукта от клиента
    """
    class Status(models.IntegerChoices):
        """
        Модель вариантов статуса готовности
        """
        READY = 1, 'Готов'
        CHEK = 2, 'Проверка'
        NOT_READY = 3, ''
    
    class Author(models.IntegerChoices):
        """
        Модкль выбора авторов
        """
        MBB = 1, 'Мартынов В.'

    name = models.CharField(max_length=100, verbose_name='Объект')
    slug = models.SlugField(max_length=100, verbose_name='URL')
    descriiption = models.TextField(verbose_name='Описание файла')
    date_order = models.DateField(verbose_name='Дата заказа')
    date_ready = models.DateField(verbose_name='Дата готовности')
    date_check = models.DateField(verbose_name='Дата Проверки')
    status = models.IntegerField(choices=Status.choices, verbose_name='Статус')
    author = models.IntegerField(choices=Author.choices, verbose_name='Автор')
    relay = models.OneToOneField(SmartRelay, on_delete=models.CASCADE, verbose_name='Тип ПЛК')
    images = ProcessedImageField(
        verbose_name='Основное фото',
        upload_to='images/product/%y/%m/%d',
        options={'quantity': 90},
        processors=[ResizeToFill(300, 300)]
    )


class Image(models.Model):
    """
    Класс описывает модель изображений для изделия
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Фото')
    image = ProcessedImageField(
        verbose_name='Фотография',
        upload_to=product_images_directory_path,
        options={'quantity': 90},
        processors=[ResizeToFill(300, 300)]
    )

    class Meta:
        db_table = 'images'
        verbose_name = 'image'
        verbose_name_plural = 'images'
