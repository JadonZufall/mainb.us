from django.db import models
from apps.authentication.models import User

class MaintenanceRecord(models.Model):
	date = models.DateField(

	)
	miles = models.IntegerField(

	)


class MaintenanceType(models.Model):
	records = models.ManyToManyField(
		MaintenanceRecord,
	)
	time_repeat = models.DurationField(
		verbose_name="Time Repeat",
		default=None,
		null=True,
		help_text="Repeat every x time passed sense this maintance was last performed."
	)
	mile_repeat = models.IntegerField(
		verbose_name="Mile Repeat",
		default=None,
		null=True,
		help_text="Repeat every time the car has passed x miles.",
	)





class Car(models.Model):
	owner = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name="owned_by",
	)
	name = models.CharField(
		verbose_name="Name",
		unique=False,
		max_length=64,
		blank=True,
		null=True,
		default="",
		editable=True,
	)
	make = models.CharField(
		verbose_name="Make",
		max_length=64,
	)
	model = models.CharField(
		verbose_name="Model",
		max_length=64,
	)
	year = models.IntegerField(
		verbose_name="Year",
	)
	plate = models.CharField(
		verbose_name="Plate",
		blank=True,
		null=True,
	)
	vin = models.CharField(
		verbose_name="VIN",
		blank=True,
		null=True,
	)
	maintenance = models.ManyToManyField(
		MaintenanceType,
		blank=True,
	)
	miles = models.IntegerField(
		verbose_name="Miles",
		blank=True,
		null=True,
		help_text="The miles that are on the car",
	)


	



