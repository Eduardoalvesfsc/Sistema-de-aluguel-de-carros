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