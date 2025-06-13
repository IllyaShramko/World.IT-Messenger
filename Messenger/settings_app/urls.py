from .views import SettingsView, AlbumsSettingsView, upload_images, delete_album, edit_album, delete_image, edit_private_album
from django.urls import path

urlpatterns = [
    path('', SettingsView.as_view(), name = 'settings'),
    path('albums/', AlbumsSettingsView.as_view(), name = 'albums'),
    path('upload/', upload_images, name = 'upload_images'),
    path('delete/<int:album_pk>', delete_album, name = 'delete_album'),
    path('delete_img/<int:img_pk>', delete_image, name = 'delete_image'),
    path('edit/<int:album_pk>', edit_album, name = 'edit_album'),
    path('change_private/<int:album_pk>', edit_private_album, name = 'album_private'),
]   