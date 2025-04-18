from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseNotFound
from django.shortcuts import render

import apps.filestore.models as models


class DeleteView(View):
	def get(self, request: HttpRequest, pk: int) -> HttpResponse:
		pass

	def post(self, request: HttpRequest, pk: int) -> HttpResponse:
		try:
			instance = models.File.objects.get(pk=pk)
		except ObjectDoesNotExist:
			return HttpResponseNotFound()
	
	def delete(self, request: HttpRequest, pk: int) -> HttpResponse:
		try:
			instance = models.File.objects.get(pk=pk)
			
		
		except ObjectDoesNotExist:
			return HttpResponseNotFound("Object not found.")
			