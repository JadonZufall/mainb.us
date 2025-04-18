from django import forms
from django.forms import ValidationError
from apps.authentication.models import User




class UserSigninForm(forms.ModelForm):
    username = forms.CharField(
        label="username",
        widget=forms.TextInput,
    )
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput,
    )