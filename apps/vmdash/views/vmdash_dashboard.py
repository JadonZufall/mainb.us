from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import resolve_url

from apps.authentication.models import User
from apps.vmdash import models

class VMDashboardView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		if not request.user.is_authenticated:
			redirect("authentication_signin")
		vehicles = models.Vehicle.objects.filter(owner=request.user)
		context = {
			"vehicles": [
				{
					"pk": vehicle.pk,
					"model": vehicle,
					"owner_name": vehicle.owner.username.capitalize(),
					"owner_url": resolve_url("authentication_user_profile", vehicle.owner.username),
					"url": "",		# TODO: Should be the link to view the car
					"status": "okay",
				}
				for vehicle in vehicles
			]
		}
		
		return render(request, "vmdash_dashboard.html", context=context)
	
	def post(self, request: HttpRequest) -> HttpResponse:
		pass