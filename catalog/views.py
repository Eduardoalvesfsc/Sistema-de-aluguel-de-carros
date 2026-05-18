from django.shortcuts import render, redirect
from .models import Carro
from .forms import CarroForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.utils import timezone
from datetime import timedelta
from .forms import ClienteForm
from .forms import AluguelForm
from django.contrib.auth.decorators import user_passes_test
from .forms import FuncionarioForm
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Aluguel
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import get_object_or_404

def carro_list(request):
    carros = Carro.objects.all()
    return render(request, 'catalog/carro_list.html', {'carros': carros})

def add_carro(request):
    if request.method =='POST':
        form = CarroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('carro_list')
    else:
        form = CarroForm()
    return render(request, 'catalog/add_carro.html', {'form': form})

def is_funcionario(user):
    return user.is_staff

@require_POST
def remover_carro(request, id):
    carro = get_object_or_404(Carro, id=id)
    carro.delete()
    return redirect('carro_list')

def carro_alugado(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)

    if carro.total_disponivel <= 0:
        messages.error(request, "Carro indisponível")
        return redirect('carro_list')

    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        form = AluguelForm(request.POST)

        if cliente_form.is_valid() and form.is_valid():

            # salva cliente
            cliente = cliente_form.save()

            # cria aluguel SEM salvar ainda
            aluguel = form.save(commit=False)
            aluguel.funcionario = request.user
            aluguel.cliente = cliente
            aluguel.carro = carro

            # validação
            if aluguel.quantidade_dias <= 0:
                messages.error(request, "Quantidade de dias deve ser maior que zero")
                return render(request, 'catalog/carro_alugado.html', {
                    'form': form,
                    'cliente_form': cliente_form
                })

            # salva aluguel
            aluguel.save()

            # atualiza estoque
            carro.total_disponivel -= 1
            carro.save()

            messages.success(request, "Aluguel realizado com sucesso!")
            return redirect('carro_list')

    else:
        form = AluguelForm()
        cliente_form = ClienteForm()

    return render(request, 'catalog/carro_alugado.html', {
        'form': form,
        'cliente_form': cliente_form
    })

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)


def cadastrar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            user = form.save()

            # adiciona ao grupo Funcionarios
            grupo, _ = Group.objects.get_or_create(name='Funcionarios')
            user.groups.add(grupo)

            return redirect('carro_list')
    else:
        form = FuncionarioForm()

    return render(request, 'funcionarios/cadastro.html', {'form': form})

def contrato_pdf(request, aluguel_id):
    aluguel = Aluguel.objects.get(id=aluguel_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="contrato.pdf"'

    p = canvas.Canvas(response)

    valor_total = aluguel.carro.valor_diaria * aluguel.quantidade_dias

    y = 800

    p.setFont("Helvetica-Bold", 16)
    p.drawString(180, y, "CONTRATO DE LOCAÇÃO")
    y -= 50

    p.setFont("Helvetica", 12)

    p.drawString(50, y, f"Cliente: {aluguel.cliente.nome}")
    y -= 25

    p.drawString(50, y, f"CPF: {aluguel.cliente.cpf}")
    y -= 25

    p.drawString(50, y, f"Telefone: {aluguel.cliente.telefone}")
    y -= 25

    p.drawString(50, y, f"E-mail: {aluguel.cliente.email}")
    y -= 40

    p.drawString(50, y, f"Veículo: {aluguel.carro.nome}")
    y -= 25

    p.drawString(50, y, f"Marca: {aluguel.carro.marca}")
    y -= 25

    p.drawString(50, y, f"Ano: {aluguel.carro.ano}")
    y -= 40

    p.drawString(50, y, f"Quantidade de dias: {aluguel.quantidade_dias}")
    y -= 25

    p.drawString(50, y, f"Valor da diária: R$ {aluguel.carro.valor_diaria}")
    y -= 25

    p.drawString(50, y, f"Valor total: R$ {valor_total}")
    y -= 25

    p.drawString(50, y, f"Forma de pagamento: {aluguel.forma_pagamento}")
    y -= 40

    p.drawString(50, y, "Assinatura do Cliente:")
    y -= 60

    p.line(50, y, 300, y)

    p.showPage()
    p.save()

    return response