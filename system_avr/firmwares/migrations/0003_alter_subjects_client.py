# Generated by Django 5.0.1 on 2024-01-25 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0002_remove_client_level_remove_client_lft_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firmwares.client', verbose_name='Клиент'),
        ),
    ]
