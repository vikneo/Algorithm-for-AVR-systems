from django import forms

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
        widget=forms.TextInput(
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
    subject = forms.CharField(
        label='Объект',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
            }
        )
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['subject'].input_value = kwargs['instance'].subject.id
        print(self.fields['subject'].input_value)

    class Meta:
        model = Product
        fields = [
            'id_product',
            'subject',
            'name',
            'relay',
            'note',

        ]
