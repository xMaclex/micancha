from django.db import models


class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to="canchas/", blank=True, null=True)
    
    def __str__(self):
        return self.nombre

    
