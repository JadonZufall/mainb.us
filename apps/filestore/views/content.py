from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render

import apps.filestore.models as models


class ContentView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		files = models.File.objects.all()
		files = [f for f in files]
		return render(request, "content.html", {"files": files})

	def post(self, request: HttpRequest) -> HttpResponse:
		pass