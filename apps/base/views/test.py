from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render



class TestView(View):
    async def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        response: HttpResponse = render(
            request,
            "test.html",
        )
        return response
    
    async def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        pass