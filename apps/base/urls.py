from django.urls import path, include
from .views.index import IndexView
from .views.test import TestView

urlpatterns = [
	path('', IndexView.as_view(), name="index"),
	path('test/', TestView.as_view(), name="test"),
]