from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class Tipo(models.Model):
	nome = models.CharField(max_length = 20)

	def __unicode__(self):
		return self.tipo

class Cerveja(models.Model):
	nome = models.CharField(max_length = 40, blank = True, null = True)
	marca = models.CharField(max_length = 40, blank = True, null = True)
	tipo = models.ManyToManyField(Tipo) 
	fornecedor = models.CharField(max_length = 120)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	preco = models.DecimalField(max_digits=5, decimal_places=2)
	quantidadeNoPacote = AutoField(max_digits = 2)
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
	dataInicio = models.DateField(auto_now = False, auto_now_add = False)
	status = models.CharField(max_length = 40)

	def __unicode__(self):
		return self.user.username

class Conteudo(models.Model):
	quantidade = models.AutoField(max_digits=6)

	def __unicode__(self):
		return self.user.username

class Itens(models.Model):
	quantidade = models.AutoField(max_digits=6)

	def __unicode__(self):
		return self.user.username

class Pedido(models.Model):
	orcamento = models.DecimalField(max_digits=8, decimal_places=2)
	data = models.DateField(auto_now = False, auto_now_add = False)
	status = models.CharField(max_length = 40)
	frete = models.DecimalField(max_digits=5, decimal_places=2)
	
	def __unicode__(self):
		return self.user.username

class Fornecedor(models.Model):
	CNPJ = models.AutoField(max_digits = 14)
	endereco = models.TextField()
	status = models.CharField(max_length = 40)
	
	def __unicode__(self):
		return self.user.username