import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = str(self.scope['url_route']['kwargs']['group_pk'])
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': "send_message_to_chat",
                'text_data': json.loads(text_data)['message'],
                'username': F"{self.scope['user'].first_name} {self.scope['user'].last_name}",
            }
        )
    
    async def send_message_to_chat(self, event):
        try:
            await self.send(
                text_data= json.dumps({
                    'type': "chat",
                    'message': {
                        'message': event['text_data'],
                        'username': event['username'],
                    },
                })
            )

        except Exception as e:
            print(f"Error in send_message_to_chat: {e}")
            return