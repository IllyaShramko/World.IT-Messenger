from django.urls import path
from .views import ChatsView, ChatView, redirect_to_personal_chat, delete_group, leave_group, get_group, edit_chat

urlpatterns = [
    path('', ChatsView.as_view(), name = "all_chats"),
    path('<int:user1_pk>/<int:user2_pk>/', redirect_to_personal_chat, name = 'personal_chat'),
    path('<int:group_pk>', ChatView.as_view(), name = 'chat'),
    path('delete_group/<int:group_pk>', delete_group, name = "delete_group"),
    path('leave_group/<int:group_pk>', leave_group, name = "leave_group"),
    path('get_group/<int:group_pk>', get_group, name="get_group"),
    path('edit_chat/<int:group_pk>', edit_chat, name="edit_chat"),
]