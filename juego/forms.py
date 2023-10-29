from django import forms
from .models import Holken

class HolkenForm(forms.ModelForm):
    class Meta:
        model = Holken
        fields = ['num_holken', 'nombre_holken', 'equipo', 'rol', 'puntos', 'avatar']
