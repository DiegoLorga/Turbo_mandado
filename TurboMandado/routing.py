
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import geolocalizacion.routing  # Importa las rutas de la app geolocalizacion
application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            geolocalizacion.routing.websocket_urlpatterns
        )
    ),
})
