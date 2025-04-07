from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect

import apps.filestore.models as models

class VideoView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        video = models.Video.objects.get(pk=pk)
        filepath = video.videofile.url
        response: HttpResponse = render(
            request, "video.html", {"filepath": filepath}
        )
        return response
    
    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        pass