from django.db import models
from django.urls import reverse

class Video(models.Model):
	title: models.CharField = models.CharField(
		max_length=50,
	)
	description: models.CharField = models.CharField(
		max_length=500,
	)
	videofile: models.FileField = models.FileField(
		upload_to="media/",
		null=True,
	)
	date_created: models.DateTimeField = models.DateTimeField(
        name="date_created",
        verbose_name="Date Created",
        auto_now_add=True,
    )
	date_altered: models.DateTimeField = models.DateTimeField(
        name="date_altered",
        verbose_name="Date Altered",
        auto_now=True,
    )

	class Meta:
		ordering = ["-date_created"]
	
	def get_absolute_url(self):
		return reverse("media:object", kwargs={"pk": self.pk})
	