# usuarios/forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User  # si usas el usuario por defecto

class ActualizacionForm(UserChangeForm):
    password = None  # Oculta el campo de contraseña en el formulario

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
