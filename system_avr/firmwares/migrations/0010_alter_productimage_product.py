# Generated by Django 5.0.1 on 2024-01-29 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0009_rename_image_productimage_remove_product_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firmwares.subjects', verbose_name='Фото'),
        ),
    ]