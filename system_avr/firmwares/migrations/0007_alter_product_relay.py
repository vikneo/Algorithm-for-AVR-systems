# Generated by Django 5.0.1 on 2024-01-29 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0006_alter_product_archive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='relay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firmwares.smartrelay', verbose_name='Тип ПЛК'),
        ),
    ]