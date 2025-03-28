import asyncio
from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest


class IndexView(View):
    async def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        response: HttpResponse = HttpResponse(
            content="<h1>Hello World!</h1>",
            headers={},
        )
        return response
    
    async def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        pass