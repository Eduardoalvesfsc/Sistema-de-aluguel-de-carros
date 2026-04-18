from django.shortcuts import render, redirect
from .models import Carro
from .forms import CarroForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.utils import timezone
from datetime import timedelta

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

    if carro.quantidade <= 0:
        messages.error(request, "Carro indisponível")
        return redirect('carro_list')

    if request.method == 'POST':
        form = AluguelForm(request.POST)
        if form.is_valid():
            aluguel = form.save(commit=False)
            
            aluguel.funcionario = request.user
            aluguel.carro = carro

            # ✅ define automaticamente a data de início
            aluguel.data_inicio = timezone.now()

            # ✅ validação profissional
            if aluguel.quantidade_dias <= 0:
                messages.error(request, "Quantidade de dias deve ser maior que zero")
                return render(request, 'catalog/carro_alugado.html', {'form': form})

            # ✅ calcula data final automaticamente
            aluguel.data_fim = aluguel.data_inicio + timedelta(days=aluguel.quantidade_dias)

            aluguel.save()

            carro.quantidade -= 1
            carro.save()

            messages.success(request, "Aluguel realizado com sucesso!")
            return redirect('carro_list')
    else:
        form = AluguelForm()

    return render(request, 'catalog/carro_alugado.html', {'form': form})