from django import forms
from .models import carro_alugado
from catalog.models import Carro
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

user = get_user_model()

class CarroAlugadoForm(forms.ModelForm):
    carro = forms.ModelChoiceField(queryset=Carro.objects.filter(total_disponivel__gt=0))

    class Meta:
        model = carro_alugado
        fields = ['carro']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = user
        fields = ["username", "email", "password1", "password2"]