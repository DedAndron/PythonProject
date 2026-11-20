from django import forms

from .models import Card_Response

class Card_Form(forms.Form):
    title = forms.CharField(label='Title',
                            max_length=100,
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(label='Description',
                                  max_length=500,
                                  widget=forms.TextInput(attrs={'class':'form-control'}))
    image = forms.ImageField(label='Image',
                             required=True,
                             widget=forms.FileInput(attrs={'class':'form-control'}))
    tags = forms.ChoiceField(label='Tags',
                             choices=Card_Response.TAG_CHOICES,
                             widget=forms.Select(attrs={'class':'form-select'})
                             )
