# Generated by Django 5.0.1 on 2024-04-26 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0014_product_id_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='firmwares.subjects', verbose_name='Объект'),
        ),
    ]
