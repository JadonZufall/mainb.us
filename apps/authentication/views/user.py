from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseForbidden
from django.http import HttpResponseGone
from django.shortcuts import render

import apps.authentication.models as models

class UserView(View):
	def get(self, request: HttpRequest, username: str) -> HttpResponse:
		try:
			user = models.User.objects.get(username=username)
			# TODO: Get
		except ObjectDoesNotExist:
			return HttpResponseNotFound("Object not found.")

	def put(self, request: HttpRequest, username: str) -> HttpResponse:
		try:
			user = models.User.objects.get(username=username)
			# TODO: Put
		except ObjectDoesNotExist:
			return HttpResponseNotFound("Object not found.")
	
	def post(self, request: HttpRequest, username: str) -> HttpResponse:
		try:
			user = models.User.objects.get(username=username)
			# TODO: Post
		except ObjectDoesNotExist:
			return HttpResponseNotFound("Object not found.")
	
	def delete(self, request: HttpRequest, username: str) -> HttpResponse:
		try:
			user = models.User.objects.get(username=username)
			if (not request.user.is_superuser) and (request.user != user):
				return HttpResponseForbidden("You do not have permission to delete this Object.")
			user.delete()
			# Returns 204 No Content to confirm we deleted the user.
			return HttpResponse(content="No Content", code=204)
		except ObjectDoesNotExist:
			return HttpResponseNotFound("Object not found.")

	def options(self, request: HttpRequest, username: str) -> HttpResponse:
		try:
			user = models.User.objects.get(username=username)
			# TODO: Options
		except ObjectDoesNotExist:
			return HttpResponseNotFound("Object not found.")

	def patch(self, request: HttpRequest, username: str) -> HttpResponse:
		try:
			user = models.User.objects.get(username=username)
			# TODO: Patch
		except ObjectDoesNotExist:
			return HttpResponseNotFound("Object not found.")
		



