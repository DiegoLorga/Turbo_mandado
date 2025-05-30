from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_mandado, name='crear_mandado'),
    
]
