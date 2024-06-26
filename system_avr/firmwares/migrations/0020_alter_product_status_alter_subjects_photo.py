# Generated by Django 5.0.1 on 2024-05-15 02:22

import firmwares.models
import imagekit.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0019_order_reestr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(choices=[(1, 'Готов'), (2, 'Проверка'), (3, 'В работе')], verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=firmwares.models.subject_images_directory_path, verbose_name='Основное фото'),
        ),
    ]
