from django import forms
from django.forms import ValidationError
from apps.authentication.models import User




class AuthSigninForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=32,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )
    password = forms.CharField(
        label="Password",
        max_length=64,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=True,
    )