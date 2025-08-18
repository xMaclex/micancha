from django.urls import path
from . import views


urlpatterns = [

    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuarios, name='login'),
    path('logout/', views.logout_usuarios, name='logout'),
    path('perfil/', views.editar_perfil, name='editar_perfil'),
]