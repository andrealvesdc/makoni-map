import datetime
from django import forms
from .models import Person
# Criação de formularios;


class FormLogin(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['name', 'email','idade','endereco']
        fields = ['user']

class FormCreateAccount(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name','email','idade','endereco','user']

