from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView

from .models import Product, Subjects


class ProductListView(ListView):
    """
    Представление Всех продуктов на странице
    """
    # model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'

    def get_queryset(self) -> QuerySet[Any]:
        """
        Возвращает queryset отфильтрованный по полю archive.
        """
        return Product.objects.filter(archive=True)


class SubjectListView(ListView):
    """
    
    """
    paginate_by = 8
    template_name = 'product/product_list.html'
    context_object_name = 'subjects'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title='Объекты'
        )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        """
        Возвращает queryset отфильтрованный по полю archive.
        """
        client_id = self.request.GET.get('client')
        if client_id is None or client_id == '0':
            return Subjects.objects.filter(archive=True)
        else:
            return Subjects.objects.filter(archive=True, client=client_id)
