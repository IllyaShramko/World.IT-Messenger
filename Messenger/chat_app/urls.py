from django.urls import path
from .views import ChatsView

urlpatterns = [
    path('', ChatsView.as_view(), name = "all_chats"),
    path('contacts/', ChatsView.as_view(), name = 'contacts')
]