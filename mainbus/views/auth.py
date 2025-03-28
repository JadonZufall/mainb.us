import asyncio
from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest

class SignupView(View):    
    async def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        pass
    
    async def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        pass


class SigninView(View):
    async def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        pass
    
    async def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        pass


class SignoutView(View):
    async def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        pass
    
    async def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        pass