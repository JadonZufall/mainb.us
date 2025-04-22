from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render


class UserProfileView(View):
    def get(self, request: HttpRequest, username: str) -> HttpResponse:
        return HttpResponse("TODO: UserProfileView")
    
    def post(self, request: HttpRequest, username: str) -> HttpResponse:
        pass