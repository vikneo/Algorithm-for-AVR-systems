from django import forms

from .models import (
    SmartRelay,
    ProductFile,
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
        self.fields['user'].empty_label = 'Выберите автора'
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
