"""
ASGI config for Messenger project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat_app.routing import ws_urlpatterns
from channels.auth import AuthMiddlewareStack



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Messenger.settings')

# Налаштування маршрутизації типів запитів
application = ProtocolTypeRouter({
    # Налаштування запиту http (якщо тип запиту http, то перенаправити на urls.py)
    "http": get_asgi_application(),
    
    "websocket": AuthMiddlewareStack( 
        URLRouter(ws_urlpatterns)
    )
})

