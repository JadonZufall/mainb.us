from django.urls import path
from .views.v1.urls import urlpatterns as v1_urlpatterns

urlpatterns = [] + v1_urlpatterns