from django.shortcuts import (render, render_to_response)
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
import datetime
from webapp.models import Usuario, Fornecedor, Cerveja, Tipo, Administrador, Pacote, Combinacao, Assinatura
from webapp.forms import UserForm, UserProfileForm, FornecedorForm, BeerForm, PacoteForm, CombinacaoForm
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView

def home(request):
	return render(request, 'webapp/home.html' , {'nome': request.user.username})

@csrf_protect
def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('webapp/login.html', c)

@csrf_protect
def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username = username, password = password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/loggedin')
	else:
		return HttpResponseRedirect('/invalid')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def loggedin(request):
	return render_to_response('webapp/loggedin.html', {'full_name': request.user.username})

def invalid(request):
	return render(request, 'webapp/invalid_login.html')

@csrf_protect
def register_user(request):
	context = RequestContext(request)

	registered = False

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()

			registered = True

		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render_to_response('webapp/register.html', {'user_form': user_form, 
		'profile_form': profile_form, 'registered': registered}, context)
			#return HttpResponseRedirect('/accounts/register_success')
			
	#args = {}
	#args.update(csrf(request))
	#args['form'] = UserCreationForm()
	#print args
	#return render_to_response('webapp/register.html', args)

def register_success(request):
	return render_to_response('webapp/register_success.html')

def cervejas(request):
	context = RequestContext(request)
	cerveja = Cerveja.objects.all()
	return render_to_response('webapp/cervejas.html', {'cerveja': cerveja}, context)

def pacotes(request):
	context = RequestContext(request)
	pacote = Pacote.objects.all()
	return render_to_response('webapp/pacotes.html', {'pacote': pacote}, context)

@csrf_protect
def add_beer(request):
	context = RequestContext(request)

	registered = False

	if request.method == 'POST':
		beer_form = BeerForm(request.POST)

		if beer_form.is_valid():

			beer = beer_form.save()
			if 'foto' in request.FILES:
				beer.foto = request.FILES['foto']

			beer.save()

			registered = True

		else:
			print beer_form.errors

	else:
		beer_form = BeerForm()

	return render_to_response('webapp/add_beer.html', {'beer_form': beer_form, 
		'registered': registered}, context)

@csrf_protect
def del_beer(request):
	return render_to_response('webapp/del_beer.html')

def change_beer(request):
	return render_to_response('webapp/change_beer.html')

@csrf_protect
def add_fornecedor(request):
	context = RequestContext(request)

	registered = False

	if request.method == 'POST':
		fornecedor_form = FornecedorForm(request.POST)

		if fornecedor_form.is_valid():

			fornecedor = fornecedor_form.save()
			fornecedor.save()

			registered = True

		else:
			print fornecedor_form.errors

	else:
		fornecedor_form = FornecedorForm()

	return render_to_response('webapp/add_fornecedor.html', {'fornecedor_form': fornecedor_form, 
		'registered': registered}, context)

@csrf_protect
def add_combinacao(request):
	context = RequestContext(request)

	registered = False

	if request.method == 'POST':
		combinacao_form = CombinacaoForm(request.POST)

		if combinacao_form.is_valid():

			combinacao = combinacao_form.save()
			combinacao.save()

			registered = True

		else:
			print combinacao_form.errors

	else:
		combinacao_form = CombinacaoForm()

	return render_to_response('webapp/add_combinacao.html', {'combinacao_form': combinacao_form, 
		'registered': registered}, context)

@csrf_protect
def add_pacote(request):
	context = RequestContext(request)

	registered = False

	if request.method == 'POST':
		pacote_form = PacoteForm(request.POST)

		if pacote_form.is_valid():

			pacote = pacote_form.save()
			pacote.save()

			registered = True

		else:
			print pacote_form.errors

	else:
		pacote_form = PacoteForm()

	return render_to_response('webapp/add_pacote.html', {'pacote_form': pacote_form, 
		'registered': registered}, context)

@csrf_protect
def assinar(request):
	context = RequestContext(request)
	if request.user.is_authenticated():
		if request.method == 'POST':
			#pacote = Pacote.objects.all()
			for pacote1 in Pacote.objects.all():
				if pacote1.nome in request.POST:
					for usuario1 in Usuario.objects.all():
						if usuario1.user.id == request.user.id:
							dataInicio = datetime.date.today()
							data = Assinatura(dataInicio = dataInicio, status = True, cliente = usuario1, pacote = pacote1)
							data.save()
							return render_to_response('webapp/assinar.html', {'nome': usuario1.user.username})
						#else:
							#return render_to_response('webapp/home.html')
				#else:
					#return render_to_response('webapp/login.html')
		else:
			return render_to_response('webapp/pacotes.html')
	else:
		c = {}
		c.update(csrf(request))
		return render_to_response('webapp/login.html', c)

def profile(request):
	return render(request, 'webapp/profile.html')

def user_assinaturas(request):
	context = RequestContext(request)
	nome = request.user.username
	assinatura = Assinatura.objects.filter(cliente__user__username = nome)
	return render_to_response('webapp/user_assinaturas.html', {'assinatura': assinatura}, context)
	
@csrf_protect
def cancel_assinatura(request):
	context = RequestContext(request)
	if request.method == 'POST':
		cancel = request.POST.getlist('checks')
		assinaturas = Assinatura.objects.filter(id__in=cancel)
		for i in assinaturas:
			i.status = False
			i.save()
		nome = request.user.username
		aux = Assinatura.objects.filter(cliente__user__username = nome)
		return render_to_response('webapp/user_assinaturas.html', {'assinatura': aux}, context)
	return render_to_response('webapp/home.html')

def show_pacote(request):
	context = RequestContext(request)
	pacote = Pacote.objects.all()
	return render_to_response('webapp/del_pacote.html', {'pacote': pacote}, context)

@csrf_protect
def del_pacote(request):
	context = RequestContext(request)
	if request.method == 'POST':
		cancel = request.POST.getlist('checks')
		pacotes = Pacote.objects.filter(id__in=cancel)
		for i in pacotes:
			i.delete()
		aux = Pacote.objects.all()
		return render_to_response('webapp/del_pacote.html', {'pacote': aux}, context)
	return render_to_response('webapp/home.html')

def update_combinacao(request):
	context = RequestContext(request)
	combinacao = Combinacao.objects.all()
	return render_to_response('webapp/combinacoes.html', {'combinacao': combinacao}, context)

@csrf_protect
def del_combinacao(request):
	context = RequestContext(request)
	if request.method == 'POST':
		cancel = request.POST.getlist('checks')
		comb = Combinacao.objects.filter(id__in=cancel)
		for i in comb:
			if i.ativo:
				i.ativo = False
			else:
				i.ativo = True
			i.save()
		aux = Combinacao.objects.all()
		return render_to_response('webapp/combinacoes.html', {'combinacao': aux}, context)
	return render_to_response('webapp/home.html')

@csrf_protect
def delete_user(request):
	return render_to_response('webapp/delete_user.html', {'full_name': request.user.username})

@csrf_protect
def delete_account(request):
	username = request.user.username
	user = User.objects.get(username=request.user.username)
	user.delete()
	return render_to_response('webapp/conta_cancelada.html', {'full_name': username})

def show_beer(request):
	context = RequestContext(request)
	cerveja = Cerveja.objects.all()
	return render_to_response('webapp/show_beer.html', {'cerveja': cerveja}, context)

@csrf_protect
def del_beer(request):
	context = RequestContext(request)
	if request.method == 'POST':
		delete = request.POST.getlist('checks')
		cervejas = Cerveja.objects.filter(id__in=delete)
		for i in cervejas:
			i.delete()
		aux = Cerveja.objects.all()
		return render_to_response('webapp/show_beer.html', {'cerveja': aux}, context)
	return render_to_response('webapp/home.html')

@csrf_protect
def change_beer(request):
	context = RequestContext(request)
	cervejas = Cerveja.objects.all()
	return render_to_response('webapp/change_beer.html', {'cerveja': cervejas}, context)

@csrf_protect
def altera_cerveja(request):
	context = RequestContext(request)
	if request.method == 'POST':
		change = request.POST.getlist('checks')
		cervejas = Cerveja.objects.filter(id__in=change)
		for i in cervejas:
			label_preco = 'preco_' + str(i.id)
			i.preco = request.POST.get(label_preco)
			i.save()
		aux = Cerveja.objects.all()
		return render_to_response('webapp/change_beer.html', {'cerveja': aux}, context)
	return render_to_response('webapp/home.html')

