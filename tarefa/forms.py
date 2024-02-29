from django import forms

class UsuarioForms(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)