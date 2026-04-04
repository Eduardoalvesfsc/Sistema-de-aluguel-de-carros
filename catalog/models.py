from django.db import models

class Carro(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    total_disponivel = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to='carros/', null=True, blank=True)

    def __str__(self):
        return self.nome