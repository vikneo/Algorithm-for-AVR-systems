from django.urls import path

from .views import (
    SubjectDetailView,
    SubjectListView,
    SearchView,
    ProductView,
    ProductListView,
    ClientListView,
    ClientAllSubjectsView,
    )

app_name = 'product'

urlpatterns = [
    path('', ClientListView.as_view(), name='clients'),
    path('client-subjects/<slug:slug>/', ClientAllSubjectsView.as_view(), name='client-subjects'),
    path('subject/', SubjectListView.as_view(), name='subject'),
    path('client/subject/<slug:slug>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('product/<slug:slug>/', ProductView.as_view(), name='product_detail'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('search/', SearchView.as_view(), name='search'),
] 
