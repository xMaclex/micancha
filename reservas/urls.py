from django.urls import path
from . import views
from .views import editar_reserva, cancelar_reserva

urlpatterns = [
    path('', views.lista_cancha, name='lista_cancha'),
    path('registro_cancha/', views.registro_cancha, name='registro_cancha'),
    path('reserva/', views.reserva_cancha, name='reserva_cancha'),
    path('historial_reservas/', views.historial_reservas, name='historial_reservas'),
    path('editar_reserva/', editar_reserva, name='editar_reserva'),
    path('cancelar_reserva/', cancelar_reserva, name='cancelar_reserva'),

    
    

]