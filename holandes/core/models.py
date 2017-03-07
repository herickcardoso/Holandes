from __future__ import unicode_literals

from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-


class Jogador(models.Model):
    nome = models.CharField('Jogador', max_length=30, null=False)
    altura = models.DecimalField('Altura', max_digits=3, decimal_places=2)
    pernaEscolha = ((u'1', u'Direita'), (u'2', u'Esquerda'), (u'3', u'Ambas'))
    pernaboa = models.CharField(max_length=1, choices=pernaEscolha)
    aniversario = models.DateTimeField('Data de Nascimento',)
    gols = models.PositiveSmallIntegerField('Gols',)
    assistencias = models.PositiveSmallIntegerField('Assistências',)
    jogos = models.PositiveSmallIntegerField('Jogos',)
    vitorias = models.PositiveSmallIntegerField('Vitórias',)
    jogopreto = models.PositiveSmallIntegerField('Vitórias',)
    jogolaranja = models.PositiveSmallIntegerField('Vitórias',)
    nota = models.DecimalField('Nota', max_digits=5, decimal_places=2)
    valor = models.DecimalField('Valor Pago', max_digits=5, decimal_places=2)


class Atributos(models.Model):
    velocidade = models.PositiveSmallIntegerField('Velocidade', max_digits=2)
    aceleracao = models.PositiveSmallIntegerField('Aceleração', max_digits=2)
    agilidade = models.PositiveSmallIntegerField('Velocidade', max_digits=2)
    driVelocidade = models.PositiveSmallIntegerField('Velocidade', max_digits=2)
    driTecnica = models.PositiveSmallIntegerField('Velocidade', max_digits=2)
    desarme = models.PositiveSmallIntegerField('Velocidade', max_digits=2)
    agilidade = models.PositiveSmallIntegerField('Velocidade', max_digits=2)
    marcacao = models.PositiveSmallIntegerField('Velocidade', max_digits=2)
    força = models.PositiveSmallIntegerField('Velocidade', max_digits=2)
    trabEquip = models.PositiveSmallIntegerField('Velocidade', max_digits=2)
    stamina = models.PositiveSmallIntegerField('Velocidade', max_digits=2)
    chutLon = models.PositiveSmallIntegerField('Velocidade', max_digits=2)
    chutFor = models.PositiveSmallIntegerField('Velocidade', max_digits=2)
    finalizacao = models.PositiveSmallIntegerField('Velocidade', max_digits=2)
    passcurto = models.PositiveSmallIntegerField('Velocidade', max_digits=2)
    passlong = models.PositiveSmallIntegerField('Velocidade', max_digits=2)
    visao = models.PositiveSmallIntegerField('Velocidade', max_digits=2)


#    valor = models.DecimalField('Valor $', max_digits=5, decimal_places=2)
#    CPU = models.PositiveSmallIntegerField('CPU',)
#    clockCPU = models.DecimalField('Clock', max_digits=5, decimal_places=2)
#    RAM = models.DecimalField('RAM', max_digits=5, decimal_places=1)
#    SO = models.CharField('S.O.', max_length=100)
#    armazenamento = models.CharField('Armazenamento', max_length=100)
#    scaleup = models.PositiveSmallIntegerField('Scale Up',)
#    scaledown = models.PositiveSmallIntegerField ( 'Scale Down',)
#    datacenters = models.PositiveSmallIntegerField( 'Datacenters',)
#    email = models.EmailField(unique=True)
#    telefone = models.CharField(max_length=20, blank=True)
#    criado_em = models.DateTimeField('criado em', auto_now_add=True)


class Jogos(models.Model):
    criado_em = models.DateTimeField('criado em', auto_now_add=True)
    golstimepreto = models.PositiveSmallIntegerField('Gols Preto',)
    golstimelaranja = models.PositiveSmallIntegerField('Gols Laranja',)

    class Meta:
        ordering = ['criado_em']
        verbose_name = (u'nome')
        verbose_name_plural = (u'nomes')

    def __unicode__(self):
        return self.nome

#    def _get_dobro_idade(self):
#    return self.idade * 2
#    dobro_idade = property(_get_dobro_idade)
