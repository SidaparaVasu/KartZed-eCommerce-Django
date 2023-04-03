from django import forms
from .models import Vendor

class registervendor(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['username', 'email', 'password']

