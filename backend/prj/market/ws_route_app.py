import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import re_path

from market.consumer import MarketConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
# django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(
        URLRouter(
           [re_path(r'market$', MarketConsumer),] 
        )
    ),
})