from django import forms


class BookForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ "class": "form-control", "placeholder": "Book's name" }))
    author = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ "class": "form-control", "placeholder": "Author" }))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Year", "min": 1900, "max": 2026}))
    publisher = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Publisher"}))
    isAvailable = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
    style = forms.FileField(required=False, widget=forms.FileInput(attrs={ "accept": "image/*"}))


class ReaderForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ "class": "form-control", "placeholder": "Reader's name" }))
    surname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ "class": "form-control", "placeholder": "Reader's surname" }))
    contacts = forms.CharField(max_length=12, widget=forms.TextInput({"class": "form-control", "placeholder": "Contacts"}))
    email = forms.EmailField(widget=forms.EmailInput({"class": "form-control", "placeholder": "Email"}))
    registrationDate = forms.DateField(widget=forms.DateInput({"class": "form-control", "placeholder": "Date of registration", "type": "date"}))
    booksTaken = forms.CharField(required=False, widget=forms.TextInput({"class": "form-control", "placeholder": "Books taken"}))
    avatar = forms.FileField(required=False, widget=forms.FileInput(attrs={"accept": "image/*"}))
