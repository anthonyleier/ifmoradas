from django.db import models
from django.contrib.auth.models import User


class Moradia(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    dono = models.IntegerField(null=True)


class Imagem(models.Model):
    imovel = models.IntegerField(null=True)
    arquivo = models.FileField(upload_to=f'imoveis/')
