import json, base64
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.core.files.base import ContentFile

from .models import ChatGroup, ChatMessage
from user_app.models import Profile, Avatar
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Подключение к WebSocket:", self.scope["path"])
        self.room_group_name = str(self.scope['url_route']['kwargs']['group_pk'])
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        print(f"Пользователь подключился к группе {self.room_group_name}")
        await self.accept()

    async def receive(self, text_data):
        print(f"Message: {text_data}")

        chat_message = await self.save_message_to_db(text_data)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': "send_message_to_chat",
                'text_data': json.loads(text_data)['message'],
                'username': f"{self.scope['user'].first_name} {self.scope['user'].last_name}",
                "message": chat_message,
                "sent_at": chat_message.sent_at.isoformat()
            }
        )

    
    async def send_message_to_chat(self, event):
        
        try:
            await self.send(
                text_data=json.dumps({
                    'type': "chat",
                    'message': {
                        'text': event['text_data'],
                        'username': event['username'],
                        "message": event["text_data"],
                        'author': await self.get_author_message(event["message"]),
                        "authorname": await self.get_authorname_message(event["message"]),
                        "avatar": await self.get_avatars_from_db(event["message"]),
                        "attached_image": await self.get_attached_img(event["message"]),
                        'sent_at': event['sent_at']
                    },
                })
            )
        except Exception as e:
            await self.send(
                text_data=json.dumps({
                    'type': "chat",
                    'message': {
                        'text': event['text_data'],
                        'username': event['username'],
                        "message": event["text_data"],
                        'author': await self.get_author_message(event["message"]),
                        "authorname": await self.get_authorname_message(event["message"]),
                        "avatar": await self.get_avatars_from_db(event["message"]),
                        'sent_at': event['sent_at']
                    },
                })
            )
            print(f"Error in send_message_to_chat: {e}")


    @database_sync_to_async
    def save_message_to_db(self, text_data):
        data = json.loads(text_data)
        print(data)
        print(11111111)
        message_text = str(data["message"])
        try:
            img = base64.b64decode(data.get('img'))
            img_type = data.get('imgType')
            django_file = ContentFile(img, name=f'fileo.{img_type}')
            print(11)
            return ChatMessage.objects.create(
                content=message_text,
                author=Profile.objects.get(user=self.scope['user']),
                chat_group=ChatGroup.objects.get(pk=self.room_group_name),
                attached_image = django_file
            )
        except:
            print(93, Exception)
            return ChatMessage.objects.create(
                content=message_text,
                author=Profile.objects.get(user=self.scope['user']),
                chat_group=ChatGroup.objects.get(pk=self.room_group_name)
            )
    @database_sync_to_async
    def get_avatars_from_db(self, message):
        user1 = message.author
        return Avatar.objects.filter(active = True).filter(shown = True).filter(profile = user1).first().image.url
    @sync_to_async
    def get_author_message(self, message):
        return f"{message.author}"
    
    @sync_to_async
    def get_authorname_message(self, message):
        return f"{message.author.user.first_name} {message.author.user.last_name}"
    @sync_to_async
    def get_attached_img(self, message: ChatMessage):
        return message.attached_image.url
    