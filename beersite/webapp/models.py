from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class Tipo(models.Model):
	nome = models.CharField(max_length = 20)

	def __unicode__(self):
		return self.tipo

class Cerveja(models.Model):
	nome = models.CharField(max_length = 40, blank = True, null = True)
	tipo = models.ManyToManyField(Tipo) 
	fornecedor = models.CharField(max_length = 120)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	last_visit = models.DateTimeField(auto_now_add = False, auto_now = True)
	descricao = models.TextField()

	def __unicode__(self):
		return self.nome

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	endereco = models.TextField()
	data_de_nascimento = models.DateField(auto_now = False, auto_now_add = False)
	preferencias_cerveja = models.ManyToManyField(Tipo)

	def __unicode__(self):
		return self.user.username
		
class Combinacao(models.Model):
	nome = models.CharField(max_length = 40, blank = True, null = True)
	status = models.CharField(max_length = 40)	
	
	def __unicode__(self):
		return self.user.username

class Pacote(models.Model):
	nome = models.CharField(max_length = 40, blank = True, null = True)
	valor = models.DecimalField(max_digits=7, decimal_places=2)
	frequencia = models.CharField(max_length = 40, blank = True, null = True)
	descricao = models.CharField(max_length = 1000, blank = True, null = True)
	
	def __unicode__(self):
		return self.user.username
		
class Assinatura(models.Model):
	dataInicio = models
