from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render


class GroupView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        pass
    
    def post(self, request: HttpRequest) -> HttpResponse:
        pass