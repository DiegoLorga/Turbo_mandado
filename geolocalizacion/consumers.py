import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GeoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.group_name = f"ubicacion_{self.user_id}"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        lat = data['lat']
        lng = data['lng']

        # Reenvía a todos los suscritos al grupo
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send_location',
                'lat': lat,
                'lng': lng,
            }
        )

    async def send_location(self, event):
        await self.send(text_data=json.dumps({
            'lat': event['lat'],
            'lng': event['lng'],
        }))
