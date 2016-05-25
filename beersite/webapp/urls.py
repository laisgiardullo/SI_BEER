"""beersite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', 'webapp.views.home'),
    url(r'^accounts/login/$', 'webapp.views.login'),
    url(r'^accounts/auth/$', 'webapp.views.auth_view'),
    url(r'^accounts/logout/$', 'webapp.views.logout'),
    url(r'^accounts/loggedin/$', 'webapp.views.loggedin'),
    url(r'^accounts/invalid/$', 'webapp.views.invalid'),
    url(r'^accounts/register/$', 'webapp.views.register_user'),
    url(r'^accounts/register_success/$', 'webapp.views.register_success'),
]
