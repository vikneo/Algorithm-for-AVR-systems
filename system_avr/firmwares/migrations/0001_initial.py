# Generated by Django 5.0.1 on 2024-01-25 04:50

import django.db.models.deletion
import firmwares.models
import imagekit.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('descriiption', models.TextField(default='', verbose_name='Описание файла')),
                ('date_order', models.DateField(verbose_name='Дата заказа')),
                ('date_ready', models.DateField(blank=True, verbose_name='Дата готовности')),
                ('date_check', models.DateField(blank=True, verbose_name='Дата Проверки')),
                ('status', models.IntegerField(choices=[(1, 'Готов'), (2, 'Проверка'), (3, '')], verbose_name='Статус')),
                ('author', models.IntegerField(choices=[(1, 'Мартынов В.')], verbose_name='Автор')),
                ('images', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/product/%y/%m/%d', verbose_name='Основное фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('availability', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='SmartRelay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend', models.CharField(max_length=100, verbose_name='Бренд')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('name', models.CharField(choices=[('ПР200', 'ПР200'), ('ПР205', 'ПР205'), ('ПР103', 'ПР103'), ('SR3B261BD', 'SR3B261BD'), ('SR2B201FU', 'SR2B201FU'), ('SR2B121FU', 'SR2B121FU'), ('Oni', 'Oni')], max_length=20, verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'реле',
                'verbose_name_plural': 'реле',
                'db_table': 'smartrelay',
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120, verbose_name='Объект')),
                ('slug', models.SlugField(max_length=120, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'объект',
                'verbose_name_plural': 'объекты',
                'db_table': 'subjects',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=firmwares.models.product_images_directory_path, verbose_name='Фотография')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firmwares.product', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'изображение',
                'verbose_name_plural': 'изображения',
                'db_table': 'images',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='relay',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='firmwares.smartrelay', verbose_name='Тип ПЛК'),
        ),
        migrations.AddField(
            model_name='product',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firmwares.subjects', verbose_name='Объект'),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Клиент')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firmwares.subjects', verbose_name='Объект')),
            ],
            options={
                'verbose_name': 'клиент(а)',
                'verbose_name_plural': 'клиенты',
                'db_table': 'clients',
            },
        ),
    ]
