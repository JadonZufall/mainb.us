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
					"instance": vehicle,
					"pk": vehicle.pk,
					"name": vehicle.name.capitalize() if vehicle.name else "<NAME>",
					"make": vehicle.make.name.capitalize() if vehicle.make else "<MAKE>",
					"model": vehicle.model.name.capitalize() if vehicle.model else "<MODEL>",
					"year": vehicle.year,
					"vin": vehicle.vin if vehicle.vin else "<VIN>",
					"plate": vehicle.plate if vehicle.plate else "<PLATE>",
					"mileage": vehicle.mileage if vehicle.mileage is not None else "<MILEAGE>",
					"owner_username": vehicle.owner.username.capitalize(),
					"url": "",		# TODO: Should be the link to view the car
					"status": "okay",
					"shared_to_edit": vehicle.shared_to_edit.all(),
					"shared_to_view": vehicle.shared_to_view.all(),
				}
				for vehicle in vehicles
			]
		}
		
		return render(request, "vmdash_dashboard.html", context=context)
	
	def post(self, request: HttpRequest) -> HttpResponse:
		pass