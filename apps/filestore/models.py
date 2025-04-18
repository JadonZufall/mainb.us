from django.db import models
from django.urls import reverse
from django.conf import settings
import datetime

def filename_format(instance, filename: str) -> str:
	filetype: str = filename.split(".")[-1].lower()
	instance.filetype = filetype
	return '{name}.{ext}'.format(name=datetime.datetime.now().strftime("%d_%m_%y"), ext=instance.filetype)


class File(models.Model):
	name = models.CharField(
		max_length=50,
	)
	desc = models.CharField(
		max_length=500,
	)
	file = models.FileField(
		upload_to=filename_format,
		null=True,
	)
	filetype = models.CharField(
		max_length=25,
	)
	views = models.PositiveBigIntegerField(
		default=0,
	)
	downloads = models.PositiveBigIntegerField(
		default=0
	)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
		on_delete=models.SET_NULL, 			# When the user who authored the file is deleted the file sets it's author to NULL.
		null=True,
	)
	date_created = models.DateTimeField(
		auto_now_add=True,
	)
	date_altered = models.DateTimeField(
		auto_now=True,
	)

	class Meta:
		ordering = ["-date_created"]


	