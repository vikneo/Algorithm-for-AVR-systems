from django.db import models
from django.urls import reverse


def path_to_file_instuction(instance, filename):
    """
    Функция генерируетт путь для сохранения файла с инструкцией
    """
    return 


class Brand(models.Model):
    """
    Клас описывает наименование производителей
    """
    name = models.CharField(max_length=80, verbose_name="Произвоодитель")
    slug = models.SlugField(max_length=80, verbose_name='URL')

    def __str__(self) -> str:
        return f"{self.name}"
    
    # def get_absolute_url(self):
    #     return reverse("brand_detail", kwargs={'slug': self.kwargs['slug']})
    
    class Meta:
        db_table = 'brands'
        verbose_name = 'модель'
        verbose_name_plural = 'модели'


class Instruction(models.Model):
    """
    Класс описывает модель файла с инструкцией.
    Составляющая (
    Наименование производителя,
    Название продукта,
    ссылка на файл
    )
    """
    brand = models.ForeignKey(Brand, verbose_name='Производитель', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Название', db_index=True)


class FileInstruction(models.Model):
    """
    Клас с файлами для модели "Instruction"
    """

    instruction = models.OneToOneField(Instruction, verbose_name="Название", on_delete=models.CASCADE)
    file = models.FileField(upload_to=path_to_file_instuction, verbose_name="Файл")

    class Meta:
        db_table = 'file_instruct'
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'
