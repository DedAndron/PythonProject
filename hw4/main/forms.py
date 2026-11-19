from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact

        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'notes'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@gmail.com'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+359 000 000 000'
            }),

            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Additional information',
                'rows': 3
            }),
        }