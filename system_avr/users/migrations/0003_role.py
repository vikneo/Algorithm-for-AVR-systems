# Generated by Django 5.0.1 on 2024-05-21 01:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_archived'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('Схемотехник', 'Crc'), ('Конструктор', 'Dsg'), ('Программист', 'Prm'), ('Отсутствует', 'Slr')], default='Отсутствует', max_length=15, verbose_name='Роль')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='users.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'роль',
                'verbose_name_plural': 'роли',
                'db_table': 'roles',
            },
        ),
    ]
