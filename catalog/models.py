from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from datetime import date

class Carro(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    total_disponivel = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to='carros/', null=True, blank=True)

    valor_diaria = models.DecimalField(max_digits=8, decimal_places=2, default=0)

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
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    carro = models.ForeignKey('Carro', on_delete=models.CASCADE)

    data_inicio = models.DateField(auto_now_add=True)
    quantidade_dias = models.IntegerField(null=True, blank=True)

    forma_pagamento = models.CharField(max_length=50, null=True, blank=True)
    observacoes = models.TextField(blank=True, null=True)

    devolvido = models.BooleanField(default=False)

    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    assinatura_cliente = models.ImageField(
    upload_to='assinaturas/',
    null=True,
    blank=True)

    @property
    def data_fim(self):
        return self.data_inicio + timedelta(days=self.quantidade_dias)

    def __str__(self):
        return f"{self.carro} - {self.cliente}"
    
    def calcular_valor(self):
        return self.quantidade_dias * self.carro.valor_diaria
    
def dashboard(request):

    total_carros = Carro.objects.count()

    carros_alugados = Aluguel.objects.filter(
        devolvido=False
    ).count()

    carros_disponiveis = Carro.objects.filter(
        total_disponivel__gt=0
    ).count()

    total_clientes = Cliente.objects.count()

    receita_total = sum(
        aluguel.carro.valor_diaria * aluguel.quantidade_dias
        for aluguel in Aluguel.objects.all()
    )

    ultimos_alugueis = (
        Aluguel.objects
        .select_related('carro', 'cliente')
        .order_by('-id')[:5]
    )

    proximas_devolucoes = (
        Aluguel.objects
        .filter(devolvido=False)
        .order_by('data_inicio')[:5]
    )

    context = {
        'total_carros': total_carros,
        'carros_alugados': carros_alugados,
        'carros_disponiveis': carros_disponiveis,
        'total_clientes': total_clientes,
        'receita_total': receita_total,
        'proximas_devolucoes': proximas_devolucoes,
    }

    return render(
        request,
        'catalog/dashboard.html',
        context
    )