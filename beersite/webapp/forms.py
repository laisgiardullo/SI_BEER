from webapp.models import Usuario
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('endereco', 'data_de_nascimento', 'CPF', 'telefone', 'n_cartao')