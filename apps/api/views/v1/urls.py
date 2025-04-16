from django.urls import path

from .u.resolve import UserResolveView
from .u.status import UserStatusView

urlpatterns = [
	path("v1/u/resolve/", UserResolveView.as_view(), name="api_v1_u_resolve"),
	path("v1/u/status/<str:username>", UserStatusView.as_view(), name="api_v1_u_status")
]