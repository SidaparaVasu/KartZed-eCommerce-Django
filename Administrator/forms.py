from django import forms
from Administrator.models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model  = Category
        fields = ('category','imagepath')