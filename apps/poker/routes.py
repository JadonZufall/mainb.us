from django.urls import path, include
from .consumers import PokerWebsocketConsumer

websocket_urlpatterns: list = [
    ('poker/', PokerWebsocketConsumer.as_asgi())
]