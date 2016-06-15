from webapp.models import Usuario, Cerveja, Fornecedor, Pacote, Combinacao
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

class BeerForm(forms.ModelForm):
	class Meta:
		model = Cerveja
		fields = ('nome', 'marca', 'tipo', 'fornecedor', 'preco', 'descricao', 'foto')

class FornecedorForm(forms.ModelForm):
	class Meta:
		model = Fornecedor
		fields = ('CNPJ', 'endereco', 'status')

class CombinacaoForm(forms.ModelForm):
   class Meta:
        model = Combinacao
        fields = ('nome', 'ativo', 'pacote', 'cervejas')

class PacoteForm(forms.ModelForm):
    class Meta:
        model = Pacote
        fields = ('nome', 'valor', 'frequencia', 'descricao', 'tipo')