from django import forms
from .models import Client


class CSVImportForm(forms.Form):
    """
    
    """
    csv_file = forms.FileField()
