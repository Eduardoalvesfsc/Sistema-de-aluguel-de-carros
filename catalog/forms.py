from django import forms
from .models import Carro
from .models import Aluguel


class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = [ "nome", "marca", "ano", "total_disponivel", "imagem"]

class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        fields = ['quantidade_dias', 'forma_pagamento', 'observacoes']

class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        fields = ['cliente', 'quantidade_dias']