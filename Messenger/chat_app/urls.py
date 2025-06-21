from django.urls import path
from .views import ChatsView, ChatView, redirect_to_personal_chat

urlpatterns = [
    path('', ChatsView.as_view(), name = "all_chats"),
    path('<int:user1_pk>/<int:user2_pk>/', redirect_to_personal_chat, name = 'personal_chat'),
    path('<int:group_pk>', ChatView.as_view(), name = 'chat')
]