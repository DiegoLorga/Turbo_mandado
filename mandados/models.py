from django.db import models
from django.contrib.auth.models import User

class Mandado(models.Model):
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mandados')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    numContacto = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.titulo} - {self.idUsuario.username}"
