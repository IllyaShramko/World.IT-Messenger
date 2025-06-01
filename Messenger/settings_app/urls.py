from .views import SettingsView
from .views import AlbumsSettingsView
from django.urls import path

urlpatterns = [
    path('', SettingsView.as_view(), name = 'settings'),
    path('albums/', AlbumsSettingsView.as_view(), name = 'albums')
]   