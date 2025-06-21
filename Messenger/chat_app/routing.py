from django.urls import path
from .consumers import ChatConsumer

ws_urlpatterns = [
    path(route = 'chats/<int:group_pk>', view = ChatConsumer.as_asgi()),
]