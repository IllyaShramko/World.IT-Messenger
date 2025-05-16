from .views import MyPostsView
from django.urls import path

urlpatterns = [
    path('my_posts/', MyPostsView.as_view(), name="my_posts" )
]