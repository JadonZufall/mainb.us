from django.db import models
from apps.authentication.models import User

from apps.location.models import Country
from apps.location.models import State


class VehicleManufacturer(models.Model):
	name = models.CharField(
		verbose_name="Name",
		unique=True,
		max_length=64,
		help_text="The name of the manufacturer.",
	)
	country = models.ForeignKey(
		Country,
		related_name="manufacturer_of",
		on_delete=models.CASCADE,
		help_text="Country that this manufacturer is located in",
	)


class VehicleMake(models.Model):
	name = models.CharField(
		verbose_name="Name",
		unique=True,
		max_length=64,
		help_text="The name of the make.",
	)

	manufacturer = models.ForeignKey(
		VehicleManufacturer,
		related_name="make_of",
		on_delete=models.CASCADE,
		help_text="Manufacturer that this make belongs to",
	)

class VehicleModel(models.Model):
	name = models.CharField(
		verbose_name="Name",
		unique=True,
		max_length=64,
		help_text="The name of the model.",
	)

	make = models.ForeignKey(
		VehicleMake,
		related_name="model_of",
		on_delete=models.CASCADE,
		help_text="Make that this model belongs to",
	)

class VehicleMaintenanceType(models.Model):
	name = models.CharField(
		verbose_name="Name",
		unique=True,
		max_length=64,
		help_text="The name of the maintenance type.",
	)

	description = models.TextField(
		verbose_name="Description",
		help_text="The description of the maintenance type.",
	)

	time_interval = models.IntegerField(
		verbose_name="Time Interval",
		help_text="The time interval of the maintenance type.",
		default=0,
	)

	miles_interval = models.IntegerField(
		verbose_name="Miles Interval",
		help_text="The miles interval of the maintenance type.",
		default=0,
	)

class VehicleMaintenanceRecord(models.Model):
	vehicle = models.ForeignKey(
		"Vehicle",
		on_delete=models.CASCADE,
		related_name="maintenance_record_of",
	)

	type = models.ForeignKey(
		VehicleMaintenanceType,
		on_delete=models.CASCADE,
		related_name="record_of",
		null=True,
		default=None,
		help_text="The type of maintenance.",
	)

	date = models.DateField(
		verbose_name="Date",
		auto_now_add=True,
	)

	miles = models.IntegerField(
		verbose_name="Miles",
		default=0,
	)

	description = models.TextField(
		verbose_name="Description",
		default="",
	)


class Vehicle(models.Model):
	owner = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name="owned_by",
	)

	name = models.CharField(
		verbose_name="Name",
		default="Unnamed Vehicle",
		max_length=64,
	)

	make = models.ForeignKey(
		VehicleMake,
		on_delete=models.SET_NULL,
		related_name="make_of",
		null=True,
	)

	model = models.ForeignKey(
		VehicleModel,
		on_delete=models.SET_NULL,
		related_name="model_of",
		null=True,
	)

	shared_to_edit = models.ManyToManyField(
		User,
		related_name="shared_to_edit_to",
		help_text="Users this vehicle is shared to, these people have permission to edit the vehicle.",
		blank=True,
	)

	shared_to_view = models.ManyToManyField(
		User,
		related_name="shared_to_view_to",
		help_text="Users this vehicle is shared to, these people have permission to view the vehicle.",
		blank=True,
	)

	vin = models.CharField(
		verbose_name="VIN",
		max_length=17,
		unique=True,
		help_text="The VIN of the vehicle.",
		blank=True,
		default="",
	)

	plate = models.CharField(
		verbose_name="Plate",
		max_length=16,
		unique=True,
		help_text="The plate of the vehicle.",
		blank=True,
		default="",
	)

	year = models.IntegerField(
		verbose_name="Year",
		help_text="The year of the vehicle.",
		default=0,
	)

	mileage = models.IntegerField(
		verbose_name="Mileage",
		help_text="The mileage of the vehicle.",
		default=0,
	)

	



