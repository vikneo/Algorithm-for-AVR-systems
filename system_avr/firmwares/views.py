from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Subjects




class SubjectListView(ListView):
    """
    
    """
    paginate_by = 8
    template_name = 'product/subject_list.html'
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


class SubjectDetailView(DetailView):
    """
    Представление Всех продуктов на странице Объекта
    """
    template_name = 'product/product_list.html'
    context_object_name = 'subject'

    def get_context_data(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context.update(
            title=kwargs['object']
        )
        print(context)
        return context

    def get_queryset(self) -> QuerySet[Any]:
        """
        Возвращает queryset отфильтрованный по полю archive.
        """
        return Subjects.objects.filter(archive=True)
