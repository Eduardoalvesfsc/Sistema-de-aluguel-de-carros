from django import forms
from .models import Carro

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ["placa", "modelo", "marca", "ano", "total_modelos", "total_disponivel"]