from django.shortcuts import render, redirect
from .models import Carro
from .forms import CarroForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

def carro_list(request):
    carros = Carro.objects.all()
    return render(request, 'catalog/carro_list.html', {'carros': carros})

def add_carro(request):
    if request.method =='POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carro_list')
    else:
        form = CarroForm()
    return render(request, 'catalog/add_carro.html', {'form': form})

def is_funcionario(user):
    return user.is_staff

def carro_alugado(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)

    if carro.total_disponivel <= 0:
        messages.error(request, "Carro indisponível no momento.")
        return redirect('carro_list')

    # lógica de aluguel
    carro.total_disponivel -= 1
    carro.save()

    messages.success(request, "Carro alugado com sucesso!")
    return redirect('meus_carros')