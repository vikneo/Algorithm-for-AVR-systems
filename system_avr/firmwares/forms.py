from django import forms

from .models import (
    ProductFile,
)


class CSVImportForm(forms.Form):
    """ """

    csv_file = forms.FileField()


class CreatedOrderForm(forms.ModelForm):
    """
    Форма для создания заявок для систем АВР
    """

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
    relay = forms.CharField(
        label='Тип реле',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                "placeholder": "например: ПР200",
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

    class Meta:
        model = ProductFile
        fields = [
            'id_product',
            'client',
            'subject',
            'name',
            'relay',
            'note',
            'file_config',
            'file_schema',
        ]
