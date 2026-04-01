from django.shortcuts import render, redirect
from .models import Carro
from .forms import CarroForm
from django.contrib.auth.decorators import login_required, user_passes_test

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

