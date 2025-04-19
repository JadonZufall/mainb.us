from django.urls import path

from .views.vmdash_dashboard import VMDashboardView

urlpatterns = [
	path("", VMDashboardView.as_view(), name="vmdash_dashboard"),
]