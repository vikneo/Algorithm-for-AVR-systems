from django.db.models.query import QuerySet
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView

from .models import Product, Subjects, Client
from utils.slugify import slugify

from typing import Any



class SubjectListView(ListView):
    """
    Представление всех объектов
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
        return Subjects.objects.filter(archive=True)


class SubjectDetailView(ListView):
    """
    Представление Всех продуктов на странице Объекта
    """
    template_name = 'product/subject_detail.html'
    context_object_name = 'products'

    def get_context_data(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context.update(
            title=kwargs,
        )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        """
        Возвращает queryset отфильтрованный по полю archive.
        """
        Subjects.objects.get(slug=self.kwargs['slug'])
        return Product.objects.filter(subject__slug=self.kwargs['slug'])


class SearchView(ListView):
    """
    Представение поискового запроса
    """
    template_name = 'product/search.html'
    context_object_name = 'seraches'
    allow_empty = True

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        try:
            context = super().get_context_data(**kwargs)
        except Exception as err:
            return Http404("Poll does not exist")
        
        context.update(
            title='Результат поиска',
        )
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        not_found = 'Нет ни одного совпадения'
        try:
            query = self.request.GET.get('search')
            search = slugify(query)
            print(search)
            result = Product.objects.filter(
                # Q(slug__icontains=search) |
                Q(id_product=search)
            )
            print(result)
            if not result:
                messages.info(self.request, not_found)
            return result
        except Exception as err:
            messages.info(self.request, not_found)
    

class ProductListView(ListView):
    """
    Представление списка всех продуктов
    """
    paginate_by = 8
    template_name = 'product/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title='Все продукты'
        )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.all().order_by('-date_ready')


class ProductView(DetailView):
    """
    Представление продукта выбранного объекта
    """
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title=kwargs['object']
        )
        return context


class ClientListView(ListView):
    """
    Представление всех клиентов
    """
    template_name = 'client/client_list.html'
    context_object_name = 'clients'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title='Клиенты'
        )
        return context
    
    def  get_queryset(self) -> QuerySet[Any]:
        client_id = self.request.GET.get('client')
        if client_id == '0' or client_id is None:
            return Client.objects.all()
        return Client.objects.filter(id=client_id)


class ClientAllSubjectsView(ListView):
    """
    Предаставление всех объектов от данного клиента
    """
    template_name = 'client/client_subjects_list.html'
    context_object_name = 'client_subjects'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        print(context['object_list'][0].id)
        context.update(
            title=kwargs,
        )
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        return Subjects.objects.filter(client__slug=self.kwargs['slug'])