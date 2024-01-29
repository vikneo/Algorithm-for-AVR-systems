from django.urls import path

from .views import ProductListView, SubjectListView

app_name = 'product'

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject')
]