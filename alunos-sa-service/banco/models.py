from django.db import models


class Conta(models.Model):
    numero = models.IntegerField()
    saldo = models.DecimalField(max_digits=11, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.numero)
