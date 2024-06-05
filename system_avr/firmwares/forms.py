from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from .models import (
    Product,
    Order
)


class CSVImportForm(forms.Form):
    """ """

    csv_file = forms.FileField()


class CreatedOrderForm(forms.ModelForm):
    """
    Форма для создания заявок для систем АВР
    """
    user = forms.CharField(
        label="Автор",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Имя Фамилия",
            },
        ),
    )
    id_product = forms.CharField(
        label="ID проекта",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "ID проекта, например 7484",
            },
        ),
    )
    client = forms.CharField(
        label='Клиент',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                "placeholder": "Клиент",
            },
        ),
    )
    subject = forms.CharField(
        label='Объект',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                "placeholder": "Название объекта",
            },
        ),
    )    
    name = forms.CharField(
        label='Название шкафа',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                "placeholder": "Название шкафа",
            },
        ),
    )
    note = forms.CharField(
        label='Примечание',
        widget=forms.Textarea(
            attrs={
                'class': 'form-input',
                'rows': 7,
                'cols': 20,
                "placeholder": "Примечание",
            },
        ),
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['relay'].empty_label = 'Выберите тип реле'
        self.fields['note'].required = False

    class Meta:
        model = Order
        fields = [
            'user',
            'id_product',
            'client',
            'subject',
            'name',
            'relay',
            'note',
            'file_schema',
        ]


class AddOrderToReestrForm(forms.ModelForm):
    """
    Форма для добавления заявки в реестр прошивок
    """
    id_product = forms.CharField(
        label="ID проекта",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
            },
        ),
    )
    client = forms.CharField(
        label='Клиент',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
            },
        ),
    )
    subject = forms.CharField(
        label='Объект',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
            },
        ),
    )    
    name = forms.CharField(
        label='Название шкафа',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
            },
        ),
    )
    note = forms.CharField(
        label='Примечание',
        widget=forms.Textarea(
            attrs={
                'class': 'form-input',
                'rows': 4,
                'cols': 20,
            },
        ),
    )
    reestr = forms.CharField(
        label='Реестр',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-input',
            },
        ),
    )
    file_schema = forms.CharField(
        label='Схема',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-input',
            },
        ),
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['note'].required = False

    class Meta:
        model = Order
        fields = [
            'id_product',
            'client',
            'subject',
            'name',
            'relay',
            'note',
            'reestr',
            'file_schema',
        ]


class ProductUpdateForm(forms.ModelForm):
    """
    Форма для редактирования Продукта
    """
    id_product = forms.CharField(
        label='ID Продукта',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
            }
        )
    )
    name = forms.CharField(
        label='Название',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
            }
        )
    )
    date_order = forms.DateField(
        label='Дата заказа',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
            }
        )
    )
    date_ready = forms.DateField(
        label='Дата готовности',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
            }
        )
    )
    date_check = forms.DateField(
        label='Дата проверки',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
            }
        )
    )
    descriiption = forms.CharField(
        label='Описание',
        widget=forms.Textarea(
            attrs={
                'class': 'form-input',
                'rows': 7,
                'cols': 20,
                "placeholder": "Тип АВР",
            },
        ),
    )
    note = forms.CharField(
        label='Примечание',
        widget=forms.Textarea(
            attrs={
                'class': 'form-input',
                'rows': 7,
                'cols': 20,
                "placeholder": "Примечание",
            },
        ),
    )
    # file_config = forms.CharField(
    #     label='Файл конфигурации',
    #     required=False,
    #     widget=forms.ClearableFileInput(
    #         attrs={
    #             'class': 'form-input',
    #         },
    #     ),
    # )
    # file_schema = forms.CharField(
    #     label='Схема',
    #     required=False,
    #     widget=forms.ClearableFileInput(
    #         attrs={
    #             'class': 'form-input',
    #         },
    #     ),
    # )
    # file_address_table = forms.CharField(
    #     label='Таблица для передачи данных',
    #     required=False,
    #     widget=forms.ClearableFileInput(
    #         attrs={
    #             'class': 'form-input',
    #         },
    #     ),
    # )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['date_ready'].required = False
        self.fields['date_check'].required = False

    class Meta:
        model = Product
        fields = [
            'id_product',
            'name',
            'relay',
            'date_order',
            'date_ready',
            'date_check',
            'status',
            'author',
            'descriiption',
            'note',
            # 'file_config',
            # 'file_schema',
            # 'file_address_table'
        ]
