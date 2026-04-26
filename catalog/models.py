from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class Carro(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    total_disponivel = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to='carros/', null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Aluguel(models.Model):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    carro = models.ForeignKey('Carro', on_delete=models.CASCADE)

    data_inicio = models.DateField(auto_now_add=True)
    quantidade_dias = models.IntegerField()

    forma_pagamento = models.CharField(max_length=50)
    observacoes = models.TextField(blank=True, null=True)

    def data_fim(self):
        return self.data_inicio + timedelta(days=self.quantidade_dias)

    def __str__(self):
        return f"{self.carro} - {self.cliente}"