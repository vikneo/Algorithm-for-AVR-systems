from django.db import models
from django.urls import reverse

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


def product_images_directory_path(instance: 'ProductImage', filename: str) -> str:
    """
    Функция генерирует путь сохранения изображений с привязкой к id товара

    :param instance: объект Image
    :param filename: имя файла
    :return: str - путь для сохранения
    """
    return f'products/product_{instance.product.name}/{filename}'

def subject_images_directory_path(instance: 'Subjects', filename: str) -> str:
    """
    
    """
    return f"subjects/{instance.name}/{filename}"


class Client(models.Model):
    """
    Класс описывает модель клиента
    """
    name = models.CharField(max_length=100, verbose_name='Клиент', db_index=True)
    slug = models.SlugField(max_length=100, verbose_name='URL', unique=True)
    description = models.TextField(verbose_name='Описание', blank=True, default="!")
    archive = models.BooleanField(default=True, verbose_name='Архив')

    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('client', kwargs={'slug': self.kwargs['slug']})

    class Meta:
        db_table = 'clients'
        verbose_name = 'клиент(а)'
        verbose_name_plural = 'клиенты'


class Subjects(models.Model):
    """
    Класс описывает модель объекта
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент', related_name='clients')
    name = models.CharField(max_length=120, verbose_name='Объект', db_index=True)
    description = models.TextField(verbose_name='Описание', blank=True, default="!")
    slug = models.SlugField(max_length=120, verbose_name='URL', unique=True)
    photo = ProcessedImageField(
        verbose_name='Основное фото',
        upload_to=subject_images_directory_path,
        options={'quantity': 90},
        processors=[ResizeToFill(600, 300)]
    )
    archive = models.BooleanField(default=True, verbose_name='Архив')


    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('subject_detail', kwargs={'slug': self.kwargs['slug']})
    
    class Meta:
        db_table = 'subjects'
        verbose_name = 'объект'
        verbose_name_plural = 'объекты'


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
        SR2B261FU = ('SR2B261FU', 'SR2B261FU')
        SR2B201FU = ('SR2B201FU', 'SR2B201FU')
        SR2B121FU = ('SR2B121FU', 'SR2B121FU')
        ONI = ('Oni', 'Oni')

    brend = models.CharField(max_length=100, verbose_name='Бренд')
    slug = models.SlugField(max_length=100, verbose_name='URL', unique=True)
    name = models.CharField(max_length=20, choices=TypeRelay, verbose_name='Модель')

    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        db_table = 'smartrelay'
        verbose_name = 'реле'
        verbose_name_plural = 'реле'


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
    id_product = models.IntegerField(verbose_name='ID Продукта', db_index=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name='Объект', related_name='subjects')
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=100, verbose_name='URL', unique=True)
    descriiption = models.TextField(verbose_name='Описание файла', blank=True, default="!")
    date_order = models.DateField(verbose_name='Дата заказа')
    date_ready = models.DateField(verbose_name='Дата готовности', blank=True, null=True)
    date_check = models.DateField(verbose_name='Дата Проверки', blank=True, null=True)
    status = models.IntegerField(choices=Status.choices, verbose_name='Статус')
    author = models.IntegerField(choices=Author.choices, verbose_name='Автор')
    relay = models.ForeignKey(SmartRelay, on_delete=models.CASCADE, verbose_name='Тип ПЛК')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    archive = models.BooleanField(default=True, verbose_name='Доступ')


    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.kwargs['slug']})

    class Meta:
        db_table = 'products'
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class ProductImage(models.Model):
    """
    Класс описывает модель изображений для изделия
    """
    product = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name='Фото')
    image = ProcessedImageField(
        verbose_name='Фотография',
        upload_to=product_images_directory_path,
        options={'quantity': 90},
        processors=[ResizeToFill(300, 300)]
    )

    class Meta:
        db_table = 'images'
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'
