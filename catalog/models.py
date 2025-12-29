from django.db import models

class Car(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=100)
    ano = models.CharField(max_length=4)
    total_modelos = models.PositiveIntegerField(default=1)
    total_disponivel = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.id:
            self.total_disponivel = self.total_modelos
        super().save(*args, **kwargs)

    def __str__(self):
        return self.modelo