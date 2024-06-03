from django.db import models
from django.urls import reverse, reverse_lazy

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from users.models import Profile


def product_images_directory_path(instance: 'ProductImage', filename: str) -> str:
    """
    Функция генерирует путь сохранения изображений

    :param instance: объект ProductImage
    :param filename: имя файла
    :return: str - путь для сохранения
    """
    return f'products/{instance.product.name}/images/{filename}'

def subject_images_directory_path(instance: 'Subjects', filename: str) -> str:
    """
    Функция генерирует путь сохранения изображений для "Объекта"

    :param instance: объект Subjects
    :param filename: имя файла
    :return: str - путь для сохранения
    """
    return f"subjects/{instance.name}/{filename}"

def product_file_path(instance: 'ProductFile', filename: str) -> str:
    """
    Функция генерирует путь сохранения файла конфигурации АВР и схемы подключения

    :param instance: объект ProductFile
    :param filename: имя файла
    :return: str - путь для сохранения
    """
    return f'products/{instance.product.name}/fiile/{filename}'

def order_file_path(instance: 'Order', filename: str) -> str:
    """
    Функция генерирует путь сохранения файла для схемы подключения и описания

    :param instance: объект Order
    :param filename: имя файла
    :return: str - путь для сохранения
    """
    return f'orders/{instance.id_product}/fiile/{filename}'


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
        blank=True,
        null=True,
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
        return f'{self.brend} - {self.name}'
    
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
        CHECK = 2, 'Проверка'
        NOT_READY = 3, 'В работе'
    
    class Author(models.IntegerChoices):
        """
        Модель выбора авторов изделия
        """
        MBB = 1, 'Мартынов В.'

    id_product = models.IntegerField(verbose_name='ID Продукта', db_index=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name='Объект', related_name='subjects')
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=100, verbose_name='URL', unique=True)
    descriiption = models.TextField(verbose_name='Описание файла', blank=True, default="Описание отсутствует!")
    date_order = models.DateField(verbose_name='Дата заказа')
    date_ready = models.DateField(verbose_name='Дата готовности', blank=True, null=True)
    date_check = models.DateField(verbose_name='Дата Проверки', blank=True, null=True)
    status = models.IntegerField(choices=Status.choices, verbose_name='Статус')
    author = models.IntegerField(choices=Author.choices, verbose_name='Автор')
    relay = models.ForeignKey(SmartRelay, on_delete=models.CASCADE, verbose_name='Тип ПЛК')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    archive = models.BooleanField(default=True, verbose_name='Доступ')
    note = models.TextField(verbose_name='Примечание', blank=True, default="Данных нет")


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


class ProductFile(models.Model):
    """
    Класс описывает файлы для модели "Product"
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Алгоритм',
        related_name='products',
        )
    file_config = models.FileField(upload_to=product_file_path, verbose_name='Конфигурация', blank=True, null=True)
    file_schema = models.FileField(upload_to=product_file_path, verbose_name='Схема с описанием')
    file_address_table = models.FileField(upload_to=product_file_path, verbose_name='Передача данных', blank=True, null=True)

    def get_absolute_url(self) -> str:
        return reverse_lazy('product:clients')
    
    class Meta:
        db_table = 'files'
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'


class Order(models.Model):
    """
    Модель для заказов систем АВР
    """
    user = models.CharField(max_length=180, verbose_name='Автор заявки')
    id_product = models.IntegerField(verbose_name='ID Продукта', db_index=True)
    client = models.CharField(max_length=100, verbose_name='Клиент')
    subject = models.CharField(max_length=100, verbose_name='Объект')
    name = models.CharField(max_length=100, verbose_name='Название')
    relay = models.ForeignKey(SmartRelay, on_delete=models.CASCADE, verbose_name='Тип ПЛК')
    note = models.TextField(verbose_name='Примечание', default='Данных нет')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    reestr = models.BooleanField(default=False, verbose_name='Реестр')
    file_schema = file_schema = models.FileField(upload_to=order_file_path, verbose_name='Схема с описанием')

    def __str__(self) -> str:
        return f"{self.id_product} - {self.name}"
    
    def get_absolute_url(self):
        return reverse_lazy('product:clients')

    class Meta:
        db_table = 'orders'
        verbose_name = 'заявку'
        verbose_name_plural = 'заявки'
