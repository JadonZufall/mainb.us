from django.urls import re_path, include
from .consumers import PokerWebsocketConsumer

websocket_urlpatterns: list = [
    re_path('ws/socket-server/', PokerWebsocketConsumer.as_asgi())
]