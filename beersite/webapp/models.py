from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class Tipo(models.Model):
	tipo = models.CharField(max_length = 20)

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
	CPF = models.CharField(max_length = 20, blank = True, null = True)
	telefone = models.CharField(max_length = 20, blank = True, null = True)
	n_cartao = models.CharField(max_length = 20, blank = True, null = True)
	
	def __unicode__(self):
		return self.user.username