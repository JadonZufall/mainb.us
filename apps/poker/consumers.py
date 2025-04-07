from typing import Any

import json
from channels.generic.websocket import WebsocketConsumer

class PokerWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()  # Accept the WebSocket connection
        self.send(text_data=json.dumps({
            "type": "connection_established",
            "message": "You are now connected!",
        }))

    def disconnect(self, close_code: Any):
        print("WebSocket disconnected")

    def receive(self, text_data):
        data: dict = json.loads(text_data)
        message = data.get('message')

        # Echo the received message back to the client
        self.send(text_data=json.dumps({
            'message': f"Echo: {message}"
        }))