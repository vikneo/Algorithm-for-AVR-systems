from django.urls import path

from .views import (
    SubjectDetailView,
    SubjectListView,
    SubjectAllProductsListView,
    SearchView,
    ProducDetailtView,
    ProductUpdateView,
    ProductListView,
    ClientListView,
    ClientAllSubjectsView,
    CreatedProductView,
    OrderListView,
    AddedOrderToReestr
    )

app_name = 'product'

urlpatterns = [
    path('', ClientListView.as_view(), name='clients'),
    path('client-subjects/<slug:slug>/', ClientAllSubjectsView.as_view(), name='client-subjects'),
    path('subjects/<int:id_product>/product-id/', SubjectAllProductsListView.as_view(), name='subject-products'),
    path('subjects/', SubjectListView.as_view(), name='subjects'),
    path('client/subject/<slug:slug>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('product/<slug:slug>/', ProducDetailtView.as_view(), name='product_detail'),
    path('product/<slug:slug>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('created/', CreatedProductView.as_view(), name='created'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('order/<int:pk>/', AddedOrderToReestr.as_view(), name='order'),
    path('search/', SearchView.as_view(), name='search'),
] 
