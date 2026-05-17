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
        fields = ['quantidade_dias', 'forma_pagamento', 'observacoes', 'assinatura_cliente']

class FuncionarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # 🔥 ESSENCIAL
        user.is_staff = True

        if commit:
            user.save()
        return user