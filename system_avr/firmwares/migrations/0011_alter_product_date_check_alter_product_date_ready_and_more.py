# Generated by Django 5.0.1 on 2024-01-30 04:03

import firmwares.models
import imagekit.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0010_alter_productimage_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_check',
            field=models.DateField(blank=True, null=True, verbose_name='Дата Проверки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_ready',
            field=models.DateField(blank=True, null=True, verbose_name='Дата готовности'),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(upload_to=firmwares.models.subject_images_directory_path, verbose_name='Основное фото'),
        ),
    ]
