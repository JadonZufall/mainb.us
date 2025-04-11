from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render


class UserView(View):
	def get(self, request: HttpRequest, username: str) -> HttpResponse:
		pass

	def put(self, request: HttpRequest, username: str) -> HttpResponse:
		pass
	
	def post(self, request: HttpRequest, username: str) -> HttpResponse:
		pass
	
	def delete(self, request: HttpRequest, username: str) -> HttpResponse:
		pass

	def options(self, request: HttpRequest, username: str) -> HttpResponse:
		pass

	def patch(self, request: HttpRequest, username: str) -> HttpResponse:
		pass



