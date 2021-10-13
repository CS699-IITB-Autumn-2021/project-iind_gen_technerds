from django import forms
from .models import *

class compressForm(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ['pdf_uploaded']
