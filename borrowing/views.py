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
