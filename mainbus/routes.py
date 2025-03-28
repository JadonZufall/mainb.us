from django.urls import path, include
from apps.poker.routes import websocket_urlpatterns as poker_websocket_urlpatterns

websocket_urlpatterns = [
    path(f'ws/poker/', poker_websocket_urlpatterns[0][1]),
]


print(websocket_urlpatterns)