from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render


class InspectPermissionView(View):
    def get(self, request: HttpRequest, permissionname: str) -> HttpResponse:
        pass
    
    def post(self, request: HttpRequest, permissionname: str) -> HttpResponse:
        pass