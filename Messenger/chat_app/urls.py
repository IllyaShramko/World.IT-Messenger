from django.urls import path
from .views import ChatsView, ChatView

urlpatterns = [
    path('', ChatsView.as_view(), name = "all_chats"),
    path('<int:user_pk>/<int:chat_pk>/', ChatView.as_view(), name = 'personal_chat'),
]