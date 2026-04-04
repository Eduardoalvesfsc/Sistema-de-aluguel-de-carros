from django import forms
from .models import Carro

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = [ "nome", "marca", "ano", "total_disponivel", "imagem"]