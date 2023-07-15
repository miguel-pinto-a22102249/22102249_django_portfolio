from django.db import models
from django.utils.html import format_html
from datetime import date

# Create your models here.

class Imagem(models.Model):
    imagem = models.ImageField(upload_to='projetos')
    nome = models.TextField(max_length=500, default='sem nome')

    def __str__(self):
        imagem_url = "/imagens/" + self.imagem.name
        return format_html(self.nome + '<br><img src="{}" height="60">', imagem_url)


class Projeto(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    descricao = models.TextField(max_length=255, null=False)
    data = models.DateField(default=date.today)
    imagens = models.ManyToManyField(Imagem, related_name='projetos')

    def __str__(self):
        return self.titulo


class Web(models.Model):
    nomeTecnologia = models.CharField(max_length=255, null=False)
    descricao = models.TextField(max_length=500, null=False)
    jaUsei = models.BooleanField(default=False)

    def __str__(self):
        return self.nomeTecnologia


class Meteorologia(models.Model):
    nome = models.CharField(max_length=100)
    temperatura = models.FloatField()
    dataHora = models.DateTimeField(null=True)

    def __str__(self):
        return self.nome

class Educacao(models.Model):
    escola = models.CharField(max_length=255, null=False)
    descricao = models.TextField(max_length=500, null=False)
    imagens = models.ManyToManyField(Imagem, related_name='educacao')

    def __str__(self):
        return self.escola


class Banda(models.Model):
    nome = models.CharField(max_length=255, null=False)
    estilo = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome

# # class Area(models.Model) :
#     nome = models.CharField(max_length=50)
#
#
# class Autor(models.Model):
#     nome = models.CharField(max_length=50)
#     areas = models.ManyToManyField(
#         Area,
#         related_name='autores'
#         )
#