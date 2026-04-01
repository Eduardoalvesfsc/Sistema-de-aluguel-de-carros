from django.db import models
from django.contrib.auth.models import User
from catalog.models import Carro
import datetime


def data_vencimento_padrao():
    return datetime.date.today() + datetime.timedelta(days=14)


class CarroAlugado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    data_aluguel = models.DateField(auto_now_add=True)
    data_vencida = models.DateField(default=data_vencimento_padrao)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.carro}"