from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Periodo(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Equipamento(models.Model):
    nome = models.CharField(max_length=25)
    ativo = models.BooleanField(default=1)

    def __str__(self):
        return self.nome


class Responsavel(models.Model):
    nome = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome


class Aula(models.Model):
    nome = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class Sala(models.Model):
    numero_sala = models.IntegerField()

    def __str__(self):
        return str(self.numero_sala)


class Agendamento(models.Model):
    data = models.DateField()
    aula = models.ForeignKey(Aula, on_delete=models.DO_NOTHING)
    periodo = models.ForeignKey(Periodo, on_delete=models.DO_NOTHING, default=1)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.DO_NOTHING, default=1)
    responsavel = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    motivo = models.TextField(blank=True)
    sala = models.ForeignKey(Sala, on_delete=models.DO_NOTHING)


