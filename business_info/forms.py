from django import forms
from .models import Business, ContactPerson

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'

class ContactPersonForm(forms.ModelForm):
    class Meta:
        model = ContactPerson
        fields = '__all__'
