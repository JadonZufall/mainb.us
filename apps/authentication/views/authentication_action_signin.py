from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from apps.authentication.forms.authentication_form_signin import AuthSigninForm


class SigninView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = AuthSigninForm()
        return render(request, "html/authentication_template_signin.html", {"form": form})
    
    def post(self, request: HttpRequest) -> HttpResponse:
        form = AuthSigninForm(request.POST)
        if not form.is_valid():
            messages.error(request, "Invalid form submission.")
            form.add_error("password", "Invalid username or password.")
            return render(request, "html/authentication_template_signin.html", {"form": form})


        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
            
        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request, user)
            return HttpResponse("Logged in successfully.")

        messages.error(request, "Invalid username or password.")
        return render(request, "html/authentication_template_signin.html", {"form": form})