from django import forms
from Administrator.models import *

class PlatformForm(forms.ModelForm):
    class Meta:
        model  = Platform
        fields = ('platform',)