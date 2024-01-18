from django.contrib import admin

from firmwares.models import Client, Product, Image, SmartRelay


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    """
    Регистрация модели "Клиент".
    """
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class AdminProduct(admin.ModelAdmin):
    """
    Регистрация модели "Product".
    """
    list_display = ['name', 'author', 'status', 'images', 'relay', 'created_at']


class AdminSmartRelay(admin.ModelAdmin):
    """
    Регистрация модели "SmartRelay".
    """
    list_display = ['brend', 'name', 'slug']
    prepopulated_fields = {'slug': ('brend',)}


admin.site.register(Product, AdminProduct)
admin.site.register(SmartRelay, AdminSmartRelay)
