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
    url(r'^home/$', 'webapp.views.home'),
    url(r'^login/$', 'webapp.views.login'),
    url(r'^auth/$', 'webapp.views.auth_view'),
    url(r'^logout/$', 'webapp.views.logout'),
    url(r'^loggedin/$', 'webapp.views.loggedin'),
    url(r'^invalid/$', 'webapp.views.invalid'),
    url(r'^register/$', 'webapp.views.register_user'),
    url(r'^register_success/$', 'webapp.views.register_success'),
    url(r'^cervejas/$', 'webapp.views.cervejas'),
    url(r'^pacotes/$', 'webapp.views.pacotes'),
    url(r'^add_beer/$', 'webapp.views.add_beer'),
    url(r'^show_beer/$', 'webapp.views.show_beer'),
    url(r'^del_beer/$', 'webapp.views.del_beer'),
    url(r'^altera_cerveja/$', 'webapp.views.altera_cerveja'),
    url(r'^change_beer/$', 'webapp.views.change_beer'),
    url(r'^add_pacote/$', 'webapp.views.add_pacote'),
    url(r'^del_pacote/$', 'webapp.views.del_pacote'),
    url(r'^show_pacote/$', 'webapp.views.show_pacote'),
    url(r'^add_fornecedor/$', 'webapp.views.add_fornecedor'),
    url(r'^add_combinacao/$', 'webapp.views.add_combinacao'),
    url(r'^assinar/$', 'webapp.views.assinar'),
    url(r'^user/profile/$', 'webapp.views.profile'),
    url(r'^user/assinaturas/$', 'webapp.views.user_assinaturas'),
    url(r'^cancel_assinatura/$', 'webapp.views.cancel_assinatura'),
    url(r'^update_combinacao/$', 'webapp.views.update_combinacao'),
    url(r'^del_combinacao/$', 'webapp.views.del_combinacao'),
    url(r'^user/delete_user/$', 'webapp.views.delete_user'),
    url(r'^user/delete_account/$', 'webapp.views.delete_account'),
]
