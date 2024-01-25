from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from django.urls import path

from .models import (
    Client, 
    Product, 
    Image, 
    SmartRelay
    )

from import_export.admin import ImportExportModelAdmin


class ImageProduct(admin.TabularInline):
    model = Image
    verbose_name = 'картинку'
    verbose_name_plural = 'картинки'
    extra = 0


@admin.register(Client)
class AdminClient(DjangoMpttAdmin, ImportExportModelAdmin):
    """
    Регистрация модели "Клиент".
    """

    list_display = ['name', 'parent', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['parent']


class AdminProduct(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Регистрация модели "Product".
    """
    inlines = [
        ImageProduct,
    ]

    list_display = ['name', 'author', 'status', 'images', 'relay', 'created_at']
    prepopulated_fields = {'slug': ('name',)}


class AdminSmartRelay(admin.ModelAdmin):
    """
    Регистрация модели "SmartRelay".
    """
    list_display = ['brend', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, AdminProduct)
admin.site.register(SmartRelay, AdminSmartRelay)
