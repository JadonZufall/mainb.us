from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect

from apps.vmdash.models import models


class VMDashCreateCarView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		if not request.user.is_authenticated:
			return redirect("authentication_signin")
		


	def post(self, request: HttpRequest) -> HttpResponse:
		pass