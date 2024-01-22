from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def check_form_csv(request: HttpRequest, form) -> HttpResponse:
    """
    Проверка на валидность формы перед загрузкой файла
    """
    if not form.is_valid():
        context = {
            'form': form,
        }
        return render(request, 'admin/csv_form.html', context)
    
    return True
