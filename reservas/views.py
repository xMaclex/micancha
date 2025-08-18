from django.shortcuts import render, redirect
from .models import Cancha
from .forms import CanchaForm


# Lista de canchas disponibles
def lista_cancha(request):
    canchas = Cancha.objects.filter(disponible=True)
    return render(request, 'reservas/lista_cancha.html', {'canchas': canchas})

def registro_cancha(request):
    if request.method == 'GET':
        form = CanchaForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('lista_cancha')
    else:
        form = CanchaForm()
    return render(request, 'reservas/registro_cancha.html', {'form': form})