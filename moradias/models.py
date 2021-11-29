from django.db import models


class Moradia(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    valor = models.DecimalField(max_digits=10, decimal_places=2)


class Imagem(models.Model):
    imovel = models.IntegerField(null=True)
    arquivo = models.FileField(upload_to='documents/%Y/%m/%d')
