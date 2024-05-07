from django.db.models.query import QuerySet
from django.db.models import Q
from django.forms import BaseModelForm
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView

from .models import (
    Product,
    Subjects,
    Client,
    Order
    )
from .forms import CreatedOrderForm
from utils.slugify import slugify

from typing import Any



class SubjectListView(ListView):
    """
    Представление всех объектов
    """
    paginate_by = 8
    template_name = 'client/client_subjects_list.html'
    context_object_name = 'client_subjects'

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
    model = Subjects
    template_name = 'product/subject_detail.html'
    context_object_name = 'products'

    def get_context_data(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context.update(
            title=self.model.objects.get(slug=self.kwargs['slug']),
        )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        """
        Возвращает queryset отфильтрованный по полю archive.
        """
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
        not_found = 'отсутствует в реестре!'
        try:
            query = self.request.GET.get('search')
            search = slugify(query)
            result = Product.objects.filter(
                # Q(slug__icontains=search) |
                Q(id_product=search)
            )
            if not result:
                messages.info(self.request, f'Номер {search} {not_found}')
            return result
        except Exception as err:
            messages.info(self.request, not_found)


class SubjectAllProductsListView(ListView):
    """
    
    """
    model = Product
    template_name = 'product/subject_products.html'
    context_object_name = 'subject_products'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title=f"ID-{self.model.objects.filter(id_product=self.kwargs['id_product'])[0].id_product}",
        )
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        return self.model.objects.filter(id_product=self.kwargs['id_product'])
    

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
    paginate_by = 10

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title='Клиенты'
        )
        return context
    
    def  get_queryset(self) -> QuerySet[Any]:
        client_id = self.request.GET.get('client')
        if client_id == '0' or client_id is None:
            return Client.objects.filter(archive=True)
        return Client.objects.filter(id=client_id, archive=True)


class ClientAllSubjectsView(ListView):
    """
    Предаставление всех объектов от данного клиента
    """
    model = Client
    template_name = 'client/client_subjects_list.html'
    context_object_name = 'client_subjects'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title=self.model.objects.get(slug=self.kwargs['slug']).name,
        )
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        return Subjects.objects.filter(client__slug=self.kwargs['slug'])


class CreatedProductView(CreateView):
    """
    Представление для создания заявок
    """
    model = Product
    form_class = CreatedOrderForm
    template_name = 'orders/create_order.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title='Заявка на АВР'
        )
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)


class OrderListView(ListView):
    """
    
    """
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title='Заявки'
        )
        return context