from bank.models import *
from django import forms
from django.forms import ModelForm

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customers
        fields='__all__'

class TransferForm(forms.ModelForm):
    class Meta:
        model=TransferTable
        fields='__all__'