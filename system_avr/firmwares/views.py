from django.db.models.query import QuerySet
from django.db.models import Q
from django.forms import BaseModelForm
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Product, ProductFile, Subjects, Client, Order
from .mixins import MenuMixin
from .forms import CreatedOrderForm, AddOrderToReestrForm, ProductUpdateForm
from .tasks import order_created
from utils.slugify import slugify

from typing import Any
from datetime import datetime


class SubjectListView(MenuMixin, ListView):
    """
    Представление всех объектов
    """

    paginate_by = 8
    template_name = "client/client_subjects_list.html"
    context_object_name = "client_subjects"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title="Объекты",
            menu=self.get_menu()
            )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        """
        Возвращает queryset отфильтрованный по полю archive.
        """
        return Subjects.objects.filter(archive=True)


class SubjectDetailView(MenuMixin, ListView):
    """
    Представление Всех продуктов на странице Объекта
    """

    model = Subjects
    template_name = "product/subject_detail.html"
    context_object_name = "products"

    def get_context_data(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context.update(
            title=self.model.objects.get(slug=self.kwargs["slug"]),
            menu=self.get_menu()
        )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        """
        Возвращает queryset отфильтрованный по полю archive.
        """
        return Product.objects.filter(subject__slug=self.kwargs["slug"])


class SearchView(MenuMixin, ListView):
    """
    Представение поискового запроса
    """

    template_name = "product/search.html"
    context_object_name = "seraches"
    allow_empty = True

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        try:
            context = super().get_context_data(**kwargs)
        except Exception as err:
            return Http404("Poll does not exist")

        context.update(
            title="Результат поиска",
            menu=self.get_menu()
        )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        not_found = "отсутствует в реестре!"
        try:
            query = self.request.GET.get("search")
            search = slugify(query)
            result = Product.objects.filter(
                # Q(slug__icontains=search) |
                Q(id_product=search)
            )
            if not result:
                messages.info(self.request, f"Номер {search} {not_found}")
            return result
        except Exception as err:
            messages.info(self.request, not_found)


class SubjectAllProductsListView(MenuMixin, ListView):
    """ """

    model = Product
    template_name = "product/subject_products.html"
    context_object_name = "subject_products"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title=f"ID-{self.model.objects.filter(id_product=self.kwargs['id_product'])[0].id_product}",
            menu=self.get_menu()
        )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        return self.model.objects.filter(id_product=self.kwargs["id_product"])


class ProductListView(MenuMixin, ListView):
    """
    Представление списка всех продуктов
    """

    paginate_by = 8
    template_name = "product/product_list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title="Все продукты",
            menu=self.get_menu()
            )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.all().order_by("-created_at")


class ProducDetailtView(MenuMixin, DetailView):
    """
    Представление продукта выбранного объекта
    """

    model = Product
    template_name = "product/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title=kwargs["object"],
            menu=self.get_menu()
            )
        return context


class ProductUpdateView(MenuMixin, UpdateView):
    """
    Обновление данных для продукта:
    - установить дату создания файла конфигурации.
    - установить дату проверки продукта.
    - изменить статус продукта.
    """
    model = Product
    template_name = "product/product_update.html"
    context_object_name = 'product'
    form_class = ProductUpdateForm
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title=f"Изменить - {self.model.objects.get(slug=self.kwargs['slug'])}",
            menu=self.get_menu()
        )

        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        try:
            return super().form_valid(form)
        except Exception as err:
            messages.warning(self.request, err)
            return HttpResponseRedirect(self.request.META.get("HTTP_REFERER"))
    
    def get_success_url(self) -> str:
        return reverse_lazy('product:product_detail', kwargs={'slug': self.kwargs['slug']})


class ClientListView(MenuMixin, ListView):
    """
    Представление всех клиентов
    """

    template_name = "client/client_list.html"
    context_object_name = "clients"
    paginate_by = 10

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title="Клиенты",
            menu=self.get_menu()
            )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        client_id = self.request.GET.get("client")
        if client_id == "0" or client_id is None:
            return Client.objects.filter(archive=True)
        return Client.objects.filter(id=client_id, archive=True)


class ClientAllSubjectsView(MenuMixin, ListView):
    """
    Предаставление всех объектов от данного клиента
    """

    model = Client
    template_name = "client/client_subjects_list.html"
    context_object_name = "client_subjects"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title=self.model.objects.get(slug=self.kwargs["slug"]).name,
            menu=self.get_menu()
        )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        return Subjects.objects.filter(client__slug=self.kwargs["slug"])


class CreatedProductView(MenuMixin, CreateView):
    """
    Представление для создания заявок
    """

    model = Order
    form_class = CreatedOrderForm
    template_name = "orders/create_order.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title="Заявка на АВР",
            menu=self.get_menu()
            )
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        order = Order.objects.create(
            user=form.cleaned_data["user"],
            id_product=form.cleaned_data["id_product"],
            client=form.cleaned_data["client"],
            subject=form.cleaned_data["subject"],
            name=form.cleaned_data["name"],
            relay=form.cleaned_data["relay"],
            note=form.cleaned_data["note"],
            file_schema=form.cleaned_data["file_schema"],
        )
        # order_created.delay(order.id) TODO добавление асинхронной задачи для отправки письма при создании заявки
        return redirect(reverse_lazy("product:orders"))


class OrderListView(MenuMixin, ListView):
    """ """

    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"
    paginate_by = 20

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title="Заявки",
            menu=self.get_menu()
            )
        return context


class AddedOrderToReestr(MenuMixin, UpdateView):
    """
    Добавление заявки в Реестр прошивок
    """

    model = Order
    form_class = AddOrderToReestrForm
    template_name = "orders/order_to_reestr.html"
    success_url = reverse_lazy("product:orders")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title="Добавить заказ в реестр",
            menu=self.get_menu()
            )
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        reestr = form.cleaned_data.get("reestr")
        if reestr:
            try:
                client = Client.objects.get_or_create(
                    name=form.cleaned_data.get("client")
                )
                subject = Subjects.objects.get_or_create(
                    client=client[0], name=form.cleaned_data.get("subject")
                )
                product = Product.objects.create(
                    id_product=form.cleaned_data.get("id_product"),
                    subject=subject[0],
                    name=form.cleaned_data.get("name"),
                    slug=form.cleaned_data.get("slug"),
                    status=3,
                    author=1,
                    date_order=datetime.today(),
                    relay=form.cleaned_data.get("relay"),
                    note=form.cleaned_data.get("note"),
                )

                ProductFile.objects.create(
                    product=product, file_schema=form.cleaned_data["file_schema"]
                )
            except Exception as err:
                messages.warning(
                    self.request,
                    f'Заявка под номером ID-{form.cleaned_data.get("id_product")} существует в "Реестр прошивок!"\n \
                    За помощью обратитесь к администратору!',
                )
                return HttpResponseRedirect(self.request.META.get("HTTP_REFERER"))

            return super().form_valid(form)
        return HttpResponseRedirect(self.request.META.get("HTTP_REFERER"))
