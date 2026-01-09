from django import forms
from main.models import *

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = "name", "specialization", "address", "website", "phone"

class SearchForm(forms.Form):
    specialization = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ "class": "form-control", "placeholder": "Specialization..." }))