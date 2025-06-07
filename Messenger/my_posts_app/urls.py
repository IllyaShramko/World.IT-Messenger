from .views import MyPostsView, delete_post, get_post, delete_img
from django.urls import path

urlpatterns = [
    path('my_posts/', MyPostsView.as_view(), name="my_posts" ),
    path('delete_post/<int:post_id>', delete_post, name= "delete_post"),
    path('edit_post/<int:post_id>', get_post, name = "edit_post"),
    path('delete_imgpost/<int:image_pk>', delete_img, name="delete_image_post")
]