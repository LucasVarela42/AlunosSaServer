from django.db import models
from banco.models import Conta


class EmpresaCerta(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=11, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
