# Generated by Django 5.0.1 on 2024-01-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0005_alter_subjects_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='archive',
            field=models.BooleanField(default=True, verbose_name='Доступ'),
        ),
    ]
