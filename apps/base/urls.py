from django.urls import path, include
from .views.index import IndexView
from .views.test import TestView
from .views.test_angular import TestAngularView

urlpatterns = [
	path('', IndexView.as_view(), name="index"),
	path('test/', TestView.as_view(), name="test"),
	path('test/angular/', TestAngularView.as_view(), name="test_angular"),
]