import json
import uuid

from django.contrib.sessions.models import Session
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        self.user = uuid.uuid4().__str__()
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": f"Welcome {self.user}", "username": self.user}
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        if message == "SEND WIZ":
            # Send message to WIZ
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "chat_wiz", "message": message, "username": self.user}
            )
        else:

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "chat_message", "message": message, "username": self.user}
            )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        user = event["username"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, "username": user}))

    async def chat_wiz(self, event):
        message = event["message"]
        user = event["username"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": "wizzzz !", "username": user}))
