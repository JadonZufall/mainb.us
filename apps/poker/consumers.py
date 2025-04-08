from typing import Any

import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class PokerWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'lobby'       # The group the user is currently apart of.
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name,
        )
        self.accept()
        self.send(text_data=json.dumps({
            "type": "connect",
            "data": "A user has connected",
        }))

    def disconnect(self, close_code: Any):
        self.send(text_data=json.dumps({
            "type": "disconnect",
            "data": "A user has disconnected",
            "code": close_code
        }))

    def receive(self, text_data):
        data: dict = json.loads(text_data)
        message = data.get('data')

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'broadcast',
                'data': message
            }
        )
    
    def broadcast(self, event):
        message = event["data"]
        self.send(text_data=json.dumps({
            "type": "broadcast",
            "data": message,
        }))