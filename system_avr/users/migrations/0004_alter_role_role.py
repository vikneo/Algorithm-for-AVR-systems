# Generated by Django 5.0.1 on 2024-06-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(blank=True, choices=[('Схемотехник', 'Схемотехник'), ('Конструктор', 'Конструктор'), ('Программист', 'Программист'), ('Отсутствует', 'Отсутствует')], default='Отсутствует', max_length=15, verbose_name='Роль'),
        ),
    ]