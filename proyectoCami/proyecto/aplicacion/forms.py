from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['alojamiento', 'texto', 'calificacion', 'usuario']

class AlojamientoForm(forms.ModelForm):
    class Meta:
        model = Alojamiento
        fields = ['titulo', 'descripcion', 'ciudad', 'direccion', 'email', 'precio']