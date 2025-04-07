from django.urls import path, include
from .views.index import IndexView

urlpatterns = [
	path('', IndexView.as_view(), name="index"),
]