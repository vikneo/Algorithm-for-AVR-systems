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

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        db_table = 'clients'
        verbose_name = 'client'
        verbose_name_plural = 'clients'


class SmartRelay(models.Model):
    """
    Класс описывает модель логических контроллеров
    """
    class TypeRelay(models.TextChoices):
        """
        Класс с выбором логичческих контроллеров.
        """
        PR200 = ('ПР200', 'ПР200')
        PR205 = ('ПР205', 'ПР205')
        PR103 = ('ПР103', 'ПР103')
        SR3B261BD = ('SR3B261BD', 'SR3B261BD')
        SR2B201FU = ('SR2B201FU', 'SR2B201FU')
        SR2B121FU = ('SR2B121FU', 'SR2B121FU')
        ONI = ('Oni', 'Oni')

    brend = models.CharField(max_length=100, verbose_name='Бренд')
    slug = models.SlugField(max_length=100, verbose_name='URL')
    name = models.CharField(max_length=20, choices=TypeRelay, verbose_name='Модель')

    def __str__(self) -> str:
        return f'{self.name}'
    
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
        Модель вариантов статуса готовности изделия
        """
        READY = 1, 'Готов'
        CHEK = 2, 'Проверка'
        NOT_READY = 3, ''
    
    class Author(models.IntegerChoices):
        """
        Модель выбора авторов изделия
        """
        MBB = 1, 'Мартынов В.'

    name = models.CharField(max_length=100, verbose_name='Объект')
    slug = models.SlugField(max_length=100, verbose_name='URL')
    descriiption = models.TextField(verbose_name='Описание файла')
    date_order = models.DateField(verbose_name='Дата заказа')
    date_ready = models.DateField(verbose_name='Дата готовности', blank=True)
    date_check = models.DateField(verbose_name='Дата Проверки', blank=True)
    status = models.IntegerField(choices=Status.choices, verbose_name='Статус')
    author = models.IntegerField(choices=Author.choices, verbose_name='Автор')
    relay = models.OneToOneField(SmartRelay, on_delete=models.CASCADE, verbose_name='Тип ПЛК')
    images = ProcessedImageField(
        verbose_name='Основное фото',
        upload_to='images/product/%y/%m/%d',
        options={'quantity': 90},
        processors=[ResizeToFill(300, 300)]
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'


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
