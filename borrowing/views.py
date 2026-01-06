from django.shortcuts import render, redirect, get_object_or_404
from .models import carro_alugado
from .forms import CarroAlugadoForm
from catalog.models import Carro
from django.contrib.auth.decorators import login_required

@login_required
def carro_alugado(request):
    if request.method == 'POST':
        form = CarroAlugadoForm(request.POST)
        if form.is_valid():
            alugado = form.save(commit=False)
            alugado.user = request.user
            alugado.save()

            # Diminuir das copias disponiveis
            carro = alugado.carro
            carro.total_disponivel -= 1
            carro.save()

            return redirect('meus_carros')
    else:
        form = CarroAlugadoForm()
    return render(request, 'borrowing/carro_alugado.html', {'form': form})

@login_required
def return_carro(request, pk):
    carro_alugado = get_object_or_404(carro_alugado, pk=pk, user=request.user, returned=False)
    carro_alugado.returned = True
    carro_alugado.save()

    # Aumenta copias disponiveis
    carro = carro_alugado.carro
    carro.total_disponivel += 1
    carro.save()

    return redirect('meus_carros')

@login_required
def meu_carros(request):
    carros_alugados = carro_alugado.objects.filter(user=request.user, returned=False)
    history = carro_alugado.objects.filter(user=request.user, returned=True).order_by('-data_aluguel')[:10]
    return render(request, 'borrowing/meus_carros.html', {
        'carros_alugados': carros_alugados,
        'history': history,
    })

@login_required
def data_vencida(request):
    vencido = carro_alugado.objetcs.filter(due_date__lt=datetime.date.today(), returned=False)
    return render(request, 'borrowing/data_vencida.html', {'data_vencida': vencido})