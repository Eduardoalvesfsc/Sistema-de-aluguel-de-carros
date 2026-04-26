from django.shortcuts import render, redirect, get_object_or_404
from .models import CarroAlugado
from .forms import CarroAlugadoForm, RegisterForm
from catalog.models import Carro
from django.contrib.auth.decorators import login_required
import datetime


@login_required
def carro_alugado(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)
    
    if request.method == 'POST':
        form = CarroAlugadoForm(request.POST)
        if form.is_valid():
            alugado = form.save(commit=False)
            alugado.user = request.user

            carro = alugado.carro

            # Evita estoque negativo
            if carro.total_disponivel > 0:
                alugado.save()

                carro.total_disponivel -= 1
                carro.save()

                return redirect('meus_carros')
            else:
                # opcional: mensagem de erro futura
                return redirect('meus_carros')
    else:
        form = CarroAlugadoForm()

    return render(request, 'borrowing/carro_alugado.html', {'form': form})


@login_required
def return_carro(request, pk):
    alugado = get_object_or_404(
        CarroAlugado,
        pk=pk,
        user=request.user,
        returned=False
    )

    alugado.returned = True
    alugado.save()

    carro = alugado.carro
    carro.total_disponivel += 1
    carro.save()

    return redirect('meus_carros')


@login_required
def meus_carros(request):
    carros_alugados = CarroAlugado.objects.filter(
        user=request.user,
        returned=False
    )

    history = CarroAlugado.objects.filter(
        user=request.user,
        returned=True
    ).order_by('-data_aluguel')[:10]

    return render(request, 'borrowing/meus_carros.html', {
        'carros_alugados': carros_alugados,
        'history': history,
    })


@login_required
def data_vencida(request):
    vencido = CarroAlugado.objects.filter(
        data_vencida__lt=datetime.date.today(),
        returned=False
    )

    return render(request, 'borrowing/data_vencida.html', {
        'data_vencida': vencido
    })


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})