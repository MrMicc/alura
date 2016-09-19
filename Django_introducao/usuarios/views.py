from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from usuarios.forms import Registrar_usuario_form
from perfis.models import Perfil

# Create your views here.
class Registrar_usuario_view(View):

    template_name = 'usuarios/registrar.html'

    def get(self, request):
        return render(request=request, template_name=self.template_name)


    def post(self, request):

        form = Registrar_usuario_form(request.POST)

        if form.is_valid():
            dados_form = form.data

            usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])
            perfil = Perfil(nome=dados_form['nome'],
                            telefone=dados_form['telefone'],
                            nome_empresa=dados_form['nome_empresa'],
                            usuario=usuario)

            perfil.save()
            return redirect('index')

        context = {
            'form':form
        }
        return render(request=request, template_name=self.template_name, context=context)