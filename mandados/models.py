from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone
from login_registro.models import Usuario

class Mandado(models.Model):
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mandados')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    numContacto = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)
    repartidor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='repartos')

def __str__(self):
    return f"{self.titulo} - {self.idUsuario.nombre}"