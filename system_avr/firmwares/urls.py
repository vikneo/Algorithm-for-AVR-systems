from django.urls import path

from .views import ProductListView, SubjectListView

app_name = 'product'

urlpatterns = [
    # path('', ProductListView.as_view(), name='index'),
    path('', SubjectListView.as_view(), name='subgect')
]