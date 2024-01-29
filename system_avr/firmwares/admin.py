from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet
from django.utils.safestring import mark_safe

from .models import (
    Client, 
    Product, 
    Image, 
    SmartRelay,
    Subjects
    )

from import_export.admin import ImportExportModelAdmin


@admin.action(description='Закрыть доступ')
def close_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archive=False)


@admin.action(description='Открыть доступ')
def open_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archive=True)



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
    actions = [
        close_access,
        open_access
    ]
    list_per_page = 15
    list_display = ['id', 'name', 'slug', 'archive']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name',]
    search_fields = ['name',]
    ordering = ('id',)


@admin.register(Subjects)
class AdminSubject(ImportExportModelAdmin, admin.ModelAdmin):
    """
    
    """
    actions = [
        close_access,
        open_access
    ]
    list_per_page = 15
    list_display = ['id', 'name', 'get_client', 'slug', 'archive']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['client',]
    list_display_links = ['name']
    search_fields = ['name',]
    ordering = ('id',)

    def get_client(self, obj: Subjects) -> str:
        """
        Возвращает название клиента для объекта.
        """
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
    actions = [
        close_access,
        open_access
    ]
    list_display = ['get_subject', 'name', 'author', 'status', 'get_images', 'relay', 'created_at', 'archive']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name',]
    save_on_top = True

    def get_subject(self, obj: Product) -> str:
        """
        Возврящает название объекта для продукта.
        """
        subject = obj.subject.name
        return subject
    
    def get_images(self, obj):
        """
        В панели администратора,
        ссылка на изображение отображается в виде картинки размером 60х 60.
        """
        return mark_safe(f'<img src="{obj.images.url}" alt="" width="60">')
    
    get_subject.short_description = 'объект'
    get_images.short_description = 'Фото'


class AdminSmartRelay(admin.ModelAdmin):
    """
    Регистрация модели "SmartRelay".
    """
    list_display = ['brend', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, AdminProduct)
admin.site.register(SmartRelay, AdminSmartRelay)
