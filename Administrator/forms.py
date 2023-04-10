from django import forms
from Administrator.models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model  = Category
        fields = ('category','imagepath')

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model  = SubCategory
        fields = ('subCategory','imagepath','category')