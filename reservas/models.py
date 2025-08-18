from django.db import models


class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to="canchas/", blank=True, null=True)

    
    def __str__(self):
        return self.nombre


class HistorialReserva(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='reservas')
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=100)  # Aquí puedes cambiar a un ForeignKey si tienes un modelo de Usuario

    def __str__(self):
        return f"Reserva de {self.cancha.nombre} por {self.usuario} el {self.fecha_reserva}"
    
