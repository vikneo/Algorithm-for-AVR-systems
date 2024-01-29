from django.urls import path

from .views import SubjectDetailView, SubjectListView

app_name = 'product'

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject'),
    path('subject/<slug:slug>', SubjectDetailView.as_view(), name='subject_detail')
]