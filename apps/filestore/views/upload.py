from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

import apps.filestore.models as models

class UploadView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		response: HttpResponse = render(
			request, "upload.html"
		)
		return response
	
	def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
		print("UPLOAD")
		title = request.POST.get("title")
		file = request.FILES.get("file")

		if file:
			video = models.Video(title=title, description="", videofile=file)
			video.save()
			return redirect(reverse("mp4", args=[video.pk]))
		else:
			return redirect(reverse("mp4", args=[video.pk]))
