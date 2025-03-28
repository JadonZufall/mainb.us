from django import forms
from django.forms import ValidationError
from .models import User


class UserSignupForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
    )
    verify_password = forms.CharField(
        label="Verify Password",
        widget=forms.PasswordInput,
    )
    
    class Meta:
        model: object = User
        fields: list[str] = ["username", "email",]
        
    def clean_password(self) -> None:
        a: str = self.cleaned_data.get("password")
        b: str = self.cleaned_data.get("verify_password")
        if a and b and a != b:
            raise ValidationError("Passwords do not match.")
        return a


class UserSigninForm(forms.ModelForm):
    pass


class UserSignoutForm(forms.ModelForm):
    pass


    