from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render


class SignoutView(View):
    def get(self, request: HttpRequest, groupname: str) -> HttpResponse:
        pass
    
    def post(self, request: HttpRequest, groupname: str) -> HttpResponse:
        pass