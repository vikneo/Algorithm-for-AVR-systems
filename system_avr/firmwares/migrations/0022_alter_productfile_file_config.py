# Generated by Django 5.0.1 on 2024-05-15 06:38

import firmwares.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0021_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfile',
            name='file_config',
            field=models.FileField(blank=True, null=True, upload_to=firmwares.models.product_file_path, verbose_name='Конфигурация'),
        ),
    ]
