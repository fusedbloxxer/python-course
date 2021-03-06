from django import forms
from django.forms import TextInput, Select

from companies.models import Companies


class CompaniesForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = ['type', 'name', 'website', 'location']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name of the company', 'class': 'form-control'}),
            'website': TextInput(attrs={'placeholder': 'Website', 'class': 'form-control'}),
            'location': Select(attrs={'class': 'form-control'}),
            'type': Select(attrs={'class': 'form-control'}),
        }
