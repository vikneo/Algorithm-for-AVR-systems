from django.urls import path

from .views import SubjectDetailView, SubjectListView,ProductView

app_name = 'product'

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject'),
    path('subject/<slug:slug>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('product/<slug:slug>/', ProductView.as_view(), name='product_detail'),
] 
