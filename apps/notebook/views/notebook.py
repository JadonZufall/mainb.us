from django.views import View
from django.http import HttpRequest
from django.http import HttpResponse

from django.shortcuts import render

class NotebookView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        pass
    
    def post(self, request: HttpRequest) -> HttpResponse:
        pass