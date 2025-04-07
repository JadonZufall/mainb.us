from django.urls import re_path, include
from apps.poker.routing import websocket_urlpatterns as poker_websocket_urlpatterns

websocket_urlpatterns = [
	*poker_websocket_urlpatterns,
]
