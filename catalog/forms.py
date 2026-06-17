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
        fields = [ "nome", "marca", "ano", "total_disponivel", "valor_diaria", "imagem"]

class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        fields = ['quantidade_dias', 'forma_pagamento', 'observacoes', 'assinatura_cliente']

from django import forms
from django.contrib.auth.models import User

class FuncionarioForm(forms.ModelForm):

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput
    )

    confirmar_password = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = super().clean()

        senha = cleaned_data.get('password')
        confirmar = cleaned_data.get('confirmar_password')

        if senha != confirmar:
            raise forms.ValidationError(
                "As senhas não coincidem."
            )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(
            self.cleaned_data['password']
        )

        user.is_staff = True
        user.is_active = True

        if commit:
            user.save()

        return user