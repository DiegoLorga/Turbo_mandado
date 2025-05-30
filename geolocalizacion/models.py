from django.db import models

# Create your models here.
class Location(models.Model):
    usuario= models.ForeignKey('login_registro.Usuario', on_delete=models.CASCADE, related_name='locations')
    latitud = models.FloatField()
    longitud = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ubicación de {self.usuario.nombre} es {self.latitud}, {self.longitud}"