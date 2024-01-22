import os
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import path

from .models import Client, Product, Image, SmartRelay
from .forms import CSVImportForm
from utils.slugify import slugify
from utils.import_csv import import_file
from utils.check_form_csv import check_form_csv

import csv



class ImageProduct(admin.TabularInline):
    model = Image
    verbose_name = 'картинку'
    verbose_name_plural = 'картинки'
    extra = 0


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    """
    Регистрация модели "Клиент".
    """
    actions = [
        "export_csv"
    ]
    change_list_template = 'admin/client_change_list.html'
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name']

    def import_csv(self, request: HttpRequest) -> HttpResponse:
        if request.method == 'GET':
            form = CSVImportForm()
            context = {
                'form': form
            }
            return render(request, 'admin/csv_form.html', context)
        
        form = CSVImportForm(request.POST, request.FILES)
        if check_form_csv(request, form):
            import_file.upload_client_csv(
                form.files["csv_file"].file,
                encoding="cp1251"
            )
        self.message_user(request, "Данные по клиентам полностью загружены!")
        return redirect('..')

    def get_urls(self):
        urls = super().get_urls()
        new_url = [
            path('import-client-csv/', self.import_csv, name='import_client_csv'),
        ]

        return new_url + urls


class AdminProduct(admin.ModelAdmin):
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
