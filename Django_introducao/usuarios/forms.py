from django import forms
from django.contrib.auth.models import User


class Registrar_usuario_form(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    telefone = forms.CharField(required=False)
    nome_empresa = forms.CharField(required=True)
    senha = forms.CharField(required=True)


    def is_valid(self):
        valid = True
        if not super(Registrar_usuario_form, self).is_valid():
            self.adiciona_erro('Favor verificar dados informados!!!')
            valid = False
        user_exist = User.objects.filter(username=self.data['email']).exists()
        if user_exist:
           self.adiciona_erro('Email ja cadastrado!!!')
           valid = False

        return valid


    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)