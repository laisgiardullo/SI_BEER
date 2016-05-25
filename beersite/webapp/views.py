from django.shortcuts import (render, render_to_response)
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm

def home(request):
	return render(request, 'webapp/home.html')

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
		return HttpResponseRedirect('/webapp/accounts/loggedin')
	else:
		return HttpResponseRedirect('/webapp/accounts/invalid')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/webapp/accounts/login')

def loggedin(request):
	return render_to_response('webapp/loggedin.html', {'full_name': request.user.username})

def invalid(request):
	return render(request, 'webapp/invalid_login.html')

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/webapp/accounts/register_success')
			
	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	print args
	return render_to_response('webapp/register.html', args)

def register_success(request):
	return render_to_response('webapp/register_success.html')