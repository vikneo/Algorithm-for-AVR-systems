from django.contrib import admin

from .models import (
    Client, 
    Product, 
    Image, 
    SmartRelay,
    Subjects
    )

from import_export.admin import ImportExportModelAdmin


class ImageProduct(admin.TabularInline):
    model = Image
    verbose_name = 'картинку'
    verbose_name_plural = 'картинки'
    extra = 0


@admin.register(Client)
class AdminClient(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Регистрация модели "Клиент".
    """

    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name',]
    search_fields = ['name',]


@admin.register(Subjects)
class AdminSubject(ImportExportModelAdmin, admin.ModelAdmin):
    """
    
    """
    list_per_page = 20
    list_display = ['id', 'name', 'get_client', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name',]
    list_display_links = ['name']
    search_fields = ['name',]
    ordering = ('id',)

    def get_client(self, obj):
        client = obj.client.name
        return client
    
    get_client.short_description = 'Клиент'


class AdminProduct(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Регистрация модели "Product".
    """
    inlines = [
        ImageProduct,
    ]

    list_display = ['name', 'author', 'status', 'images', 'relay', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name',]
    save_on_top = True


class AdminSmartRelay(admin.ModelAdmin):
    """
    Регистрация модели "SmartRelay".
    """
    list_display = ['brend', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, AdminProduct)
admin.site.register(SmartRelay, AdminSmartRelay)
