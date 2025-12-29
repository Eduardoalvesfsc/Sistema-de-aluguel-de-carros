from django.db import models
from django.contrib.auth.models import User
from catalog.models import Carro
import datetime

class carro_alugado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    data_aluguel = models.DateField(auto_now_add=True)
    data_vencida = models.DateField(default=datetime.date.today() + datetime.timedelta(days=14))
    retorno = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.carro}"