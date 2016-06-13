from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class Tipo(models.Model):
	tipo = models.CharField(max_length = 20)

	def __unicode__(self):
		return self.tipo

class Cerveja(models.Model):
	nome = models.CharField(max_length = 40, blank = True, null = True)
	marca = models.CharField(max_length = 40, blank = True, null = True)
	tipo = models.ManyToManyField(Tipo) 
	fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
	preco = models.DecimalField(max_digits=5, decimal_places=2, null = True)
	descricao = models.TextField()
	foto = models.ImageField(upload_to='imagem_cerveja', blank=True)

	def __unicode__(self):
		return self.nome

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	endereco = models.TextField()
	data_de_nascimento = models.DateField(auto_now = False, auto_now_add = False)
	CPF = models.CharField(max_length = 20, blank = True, null = True)
	telefone = models.CharField(max_length = 20, blank = True, null = True)
	n_cartao = models.CharField(max_length = 20, blank = True, null = True)
	user.is_staff = False
	
	def __unicode__(self):
		return self.user.username

class Administrador(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	CPF = models.CharField(max_length = 20, blank = True, null = True)
	user.is_staff = True

	def __unicode__(self):
		return self.user.username

		
class Combinacao(models.Model):
	nome = models.CharField(max_length = 20, blank = True, null = True)
	ativo = models.NullBooleanField()
	pacote = models.ForeignKey('Pacote', on_delete=models.CASCADE)
	cervejas = models.ManyToManyField(Cerveja)

	def __unicode__(self):
		return self.nome

class Pacote(models.Model):
	nome = models.CharField(max_length = 40, blank = True, null = True)
	valor = models.DecimalField(max_digits=7, decimal_places=2)
	frequencia = models.CharField(max_length = 40, blank = True, null = True)
	descricao = models.CharField(max_length = 1000, blank = True, null = True)
	tipo = models.ManyToManyField(Tipo)

	def __unicode__(self):
		return self.nome

class Assinatura(models.Model):
	dataInicio = models.DateField(auto_now = False, auto_now_add = False)
	status = models.NullBooleanField()
	cliente = models.ForeignKey('Usuario', on_delete=models.CASCADE)
	pacote = models.ForeignKey('Pacote', on_delete=models.CASCADE)

	def __unicode__(self):
		return self.dataInicio

class Conteudo(models.Model):
	quantidade = models.DecimalField(max_digits = 4, decimal_places = 0)

	def __unicode__(self):
		return self.quantidade

class Itens(models.Model):
	quantidade = models.DecimalField(max_digits = 2, decimal_places = 0)

	def __unicode__(self):
		return self.quantidade

class Pedido(models.Model):
	orcamento = models.DecimalField(max_digits=8, decimal_places=2)
	data = models.DateField(auto_now = False, auto_now_add = False)
	status = models.CharField(max_length = 40)
	frete = models.DecimalField(max_digits=5, decimal_places=2)
	
	def __unicode__(self):
		return self.data

class Fornecedor(models.Model):
	CNPJ = models.CharField(max_length = 40)
	endereco = models.TextField()
	status = models.CharField(max_length = 40)
	
	def __unicode__(self):
		return self.CNPJ