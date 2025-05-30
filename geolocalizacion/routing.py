from django.urls import re_path
from . import consumers  

websocket_urlpatterns = [
    re_path(r'ws/ubicacion/(?P<user_id>\d+)/$', consumers.GeoConsumer.as_asgi()),
]
