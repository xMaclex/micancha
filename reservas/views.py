from django.shortcuts import render
from .models import Cancha

# Lista de canchas disponibles
def lista_cancha(request):
    canchas = Cancha.objects.filter(disponible=True)
    return render(request, 'reservas/lista_cancha.html', {'canchas': canchas})

# Detalle de una cancha específica
