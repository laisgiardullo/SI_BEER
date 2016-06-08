from django.shortcuts import (render, render_to_response)
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from webapp.models import Usuario
from webapp.forms import UserForm, UserProfileForm
from django.template import RequestContext

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
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

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