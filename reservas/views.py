from django.shortcuts import render, redirect, get_object_or_404
from .models import Cancha, HistorialReserva
from .forms import CanchaForm
from django.contrib import messages
from datetime import datetime


# Lista de canchas disponibles
def lista_cancha(request):
    canchas = Cancha.objects.filter(disponible=True)
    return render(request, 'reservas/lista_cancha.html', {'canchas': canchas})

def registro_cancha(request):
    if request.method == "POST":
        form = CanchaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "¡La cancha se ha registrado correctamente!")
            return redirect('lista_cancha')
        else:
            messages.error(request, "Por favor corrige los errores del formulario.")
    else:
        form = CanchaForm()

    return render(request, "reservas/registro_cancha.html", {"form": form})


def reserva_cancha(request):
    if request.method == "POST":
        cancha_id = request.POST.get("cancha_id")
        cancha = get_object_or_404(Cancha, id=cancha_id)
        if cancha.disponible:
            cancha.disponible = False
            cancha.save()
            # Guardar en historial
            HistorialReserva.objects.create(cancha=cancha, usuario=request.user)
            messages.success(request, f"¡La reserva para {cancha.nombre} se ha realizado correctamente!")
        else:
            messages.error(request, f"La cancha {cancha.nombre} no está disponible.")
        return redirect('lista_cancha')
    
    canchas = Cancha.objects.filter(disponible=True)
    return render(request, 'reservas/reserva_cancha.html', {'canchas': canchas})



def historial_reservas(request):
    reservas = HistorialReserva.objects.filter(usuario=request.user).order_by('-fecha_reserva')
    return render(request, 'reservas/historial_reservas.html', {'reservas': reservas})



def editar_reserva(request):
    if request.method == "POST":
        cancha_id = request.POST.get("cancha_id")
        fecha_nueva = request.POST.get("fecha_reserva")

        reserva = get_object_or_404(HistorialReserva, cancha_id=cancha_id, usuario=request.user)

        if fecha_nueva:
            # Convertir el string a datetime
            try:
                fecha_dt = datetime.strptime(fecha_nueva, "%Y-%m-%dT%H:%M")
                reserva.fecha_reserva = fecha_dt
                reserva.save()
                messages.success(request, f"La reserva de {reserva.cancha.nombre} se actualizó correctamente.")
            except ValueError:
                messages.error(request, "Formato de fecha inválido.")
    
    return redirect("historial_reservas")


def cancelar_reserva(request):
    if request.method == "POST":
        cancha_id = request.POST.get("cancha_id")
        reserva = get_object_or_404(HistorialReserva, cancha_id=cancha_id, usuario=request.user)
        
        # Marcar la cancha como disponible nuevamente
        reserva.cancha.disponible = True
        reserva.cancha.save()
        
        # Eliminar la reserva
        reserva.delete()
        messages.success(request, f"La reserva de {reserva.cancha.nombre} ha sido cancelada.")
    
    return redirect("historial_reservas")
