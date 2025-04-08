from django.urls import path, include
from .views.content import ContentView
from .views.upload import UploadView
from .views.video import VideoView

urlpatterns = [
	path("", ContentView.as_view(), name="content"),
	path("upload/", UploadView.as_view(), name="upload"),
	path("mp4/<int:pk>/", VideoView.as_view(), name="mp4"),
]