from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Date of Birth'
    )
    connected_year = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': '1900', 'max': '2099', 'step': '1'}),
        initial=2023
    )
    mobile_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. +1234567890'}))
    whatsapp_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. +1234567890'})
    )

    class Meta:
        model = Contact
        fields = [
            'name', 'category', 'profession', 'dob', 'connected_year', 'connected_source',
            'working_place', 'native_place', 'mobile_number', 'whatsapp_number', 'email',
            'scope', 'status'
        ]
