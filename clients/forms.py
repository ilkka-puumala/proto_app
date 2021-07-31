from django import forms
from django.forms import ModelForm

from .models import Clients

class ClientForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Name of the client"}))
    short_code = forms.CharField(label='Code from the ads campaigns', widget=forms.TextInput(attrs={"placeholder": "CLI"}))

    class Meta:
        model = Clients
        fields = [
        'name',
        'short_code',
        'is_active',
        ]