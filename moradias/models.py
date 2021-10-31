from django.db import models

class Moradia(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imagem1 = models.CharField(max_length=500)
    imagem2 = models.CharField(max_length=500)
    imagem3 = models.CharField(max_length=500)