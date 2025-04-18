from django.urls import path, include
from .views.filestore import ContentView
from .views.filestore_action_upload import UploadView
from .views.filestore_inspect_video import VideoView

#f/
urlpatterns = [
	path("", ContentView.as_view(), name="home"),
	path("delete/", None, name="delete_file"),
	path("upload/", UploadView.as_view(), name="upload_file"),
	path("image/<int:pk>/", VideoView.as_view(), name="inspect_image"), #todo - change view
	path("other/<int:pk>/", VideoView.as_view(), name="inspect_other"),
	path("audio/<int:pk>/", VideoView.as_view(), name="inspect_audio"), #todo - change view
	path("video/<int:pk>/", VideoView.as_view(), name="inspect_video"),
]