from django.db import models
from django.conf import settings
# Create your models here.



class UserReport(models.Model):
	reported_user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name="reported_by",
		on_delete=models.CASCADE,
		verbose_name="Reported User",
		help_text="The user who was reported.",
	)
	reporting_user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name="reports_made",
		on_delete=models.CASCADE,
		verbose_name="Reporting User",
		help_text="The user who filed the report.",
	)
	report_reason = models.TextField(
		verbose_name="Reason for Report",
		help_text="Explanation of why the user is being reported.",
		max_length=1024,
	)
	status = models.CharField(
		max_length=32,
		choices=[
			("pending", "Pending"),
			("in_progress", "In Progress"),
			("resolved", "Resolved"),
			("dismissed", "Dismissed"),
		],
		default="pending",
		verbose_name="Status",
		help_text="The current status of the report."
	)
	resolution_user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name="resolved_by",
		on_delete=models.SET_NULL,
		verbose_name="Resolution User",
		help_text="The staff member that resolved this report.",
	)
	resolution_notes = models.TextField(
		blank=True,
		null=True,
		verbose_name="Resolution Notes",
		help_text="Notes on how the report was resolved.",
		max_length=1024,
	)

	date_created = models.DateTimeField(auto_now_add=True)
	date_altered = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "User Report"
		verbose_name_plural = "User Reports"


class UserSupportTicket(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	helper = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)


	status = models.CharField(
		max_length=32,
		choices=[
			("pending", "Pending"),
			("on_going", "On Going"),
			("closed", "Closed"),
		]
	)

	date_created = models.DateTimeField(auto_now_add=True)
	date_altered = models.DateTimeField(auto_now=True)
