from django import forms
from .models import Carro
from .models import Aluguel
from .models import Cliente
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone', 'email']

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = [ "nome", "marca", "ano", "total_disponivel", "imagem"]

class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        fields = ['quantidade_dias', 'forma_pagamento', 'observacoes']

class FuncionarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']