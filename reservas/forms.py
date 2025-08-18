from django import forms
from .models import Cancha


class CanchaForm(forms.ModelForm):
    class Meta :
        model = Cancha
        fields = ['nombre', 'descripcion', 'precio', 'disponible', 'imagen',]
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
        labels = {
            'nombre': 'Nombre de la cancha',
            'descripcion': 'Descripción',
            'disponible': '¿Disponible?',
        }