from django.urls import path
from . import views
urlpatterns = [
    path('', views.geolocalizacion_view, name='geolocalizacion_view'),
    path('seguimiento/<int:repartidor_id>/', views.seguimiento_view, name='seguimiento'),
]