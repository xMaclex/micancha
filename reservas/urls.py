from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cancha, name='lista_cancha'),
    path('registro_cancha/', views.registro_cancha, name='registro_cancha'),
]