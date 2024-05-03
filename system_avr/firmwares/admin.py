from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet
from django.utils.safestring import mark_safe

from .models import (
    Client, 
    Product, 
    ProductImage, 
    SmartRelay,
    Subjects,
    ProductFile,
    Order
    )
from utils.config import (
    LENGTH,
    get_count_for_id,
    )

from import_export.admin import ImportExportModelAdmin


@admin.action(description='Закрыть доступ')
def close_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archive=False)


@admin.action(description='Открыть доступ')
def open_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archive=True)


class ProductFileTabular(admin.TabularInline):
    model = ProductFile
    verbose_name = 'файл'
    verbose_name_plural = 'файлы'
    extra = 0


class ImageSubject(admin.TabularInline):
    model = ProductImage
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


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    """
    
    """
    list_display = ['user', 'id_product', 'get_client', 'get_subject', 'name', 'created_at', 'file_schema']
    list_filter = ['id_product']
    search_fields = ['id_product']
    ordering = ('id_product', )
    list_per_page = 15

    def get_client(self, obj: Order) -> str:
        return obj.client if len(obj.client) < LENGTH else obj.client[:LENGTH]
    
    def get_subject(self, obj: Order) -> str:
        return obj.client if len(obj.client) < LENGTH else obj.client[:LENGTH]
    
    get_client.short_description = 'Клиент'
    get_subject.short_description = 'Объект'


@admin.register(Subjects)
class AdminSubject(ImportExportModelAdmin, admin.ModelAdmin):
    """
    
    """
    inlines = [
        ImageSubject,
    ]
    actions = [
        close_access,
        open_access
    ]
    list_per_page = 15
    list_display = ['name', 'get_client', 'get_images', 'slug', 'archive']
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
        
    def get_images(self, obj):
        """
        В панели администратора,
        ссылка на изображение отображается в виде картинки размером 60х 60.
        """
        return mark_safe(f'<img src="{obj.photo.url}" alt="" width="40">')
    
    get_client.short_description = 'Клиент'
    get_images.short_description = 'Фото'


class AdminProduct(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Регистрация модели "Product".
    """
    inlines = [
        ProductFileTabular,
    ]
    actions = [
        close_access,
        open_access
    ]
    list_per_page = 40
    list_display = ['get_id_product', 'get_subject', 'get_name', 'status', 'relay', 'archive']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['id_product']
    search_fields = ['id_product', 'name',]
    save_on_top = True

    def get_id_product(self, obj: Product) -> str:
        """
        Возвращает строку с номером родукта длиной 5 регистров
        """
        product_id = str(obj.id_product)
        return get_count_for_id(product_id)

    def get_subject(self, obj: Product) -> str:
        """
        Возврящает название объекта для продукта.
        """
        subject = obj.subject.name
        return subject if len(subject) < LENGTH else subject[:LENGTH] + '...'
    
    def get_name(self, obj: Product) -> str:
        """
        Возвращает обрезаную строку названия продукта
        """
        product_name = obj.name
        return product_name if len(product_name) < LENGTH else product_name[:LENGTH] + '...'
    
    get_subject.short_description = 'объект'
    get_name.short_description = 'название'
    get_id_product.short_description = 'ID Продукт'


class AdminSmartRelay(admin.ModelAdmin):
    """
    Регистрация модели "SmartRelay".
    """
    list_display = ['brend', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, AdminProduct)
admin.site.register(SmartRelay, AdminSmartRelay)
