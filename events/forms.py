from django import forms
from django.forms import ModelForm
from .models import Venue, MyClubUser

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ["name", "address", "zip_code", "phone", "web", "emailadress"]
        labels = {
            "name": '',
            "address": '',
            "zip_code": '',
            "phone": '',
            "web": '',
            "emailadress": '',
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Venue Name"}),
            "address": forms.TextInput(attrs={"class": "form-control", "placeholder": "Address"}),
            "zip_code": forms.TextInput(attrs={"class": "form-control", "placeholder": "Zip Code"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone"}),
            "web": forms.URLInput(attrs={"class": "form-control", "placeholder": "Web"}),
            "emailadress": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
        }

class MessageForm(ModelForm):
    class Meta:
        model = MyClubUser
        fields = ["first_name", "last_name", "email", "message"]
        labels = {
            "first_name": '',
            "last_name": '',
            "email": '',
            "message": '',
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email Address"}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "Your Message", "rows":3}),
        }