from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_id', 'contact_name', 'contact_email', 'contact_message']