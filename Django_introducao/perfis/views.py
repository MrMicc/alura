from django.shortcuts import render
from perfis.models import Perfil

# Create your views here.

def index(request):
    """Delcaração de função de view"""
    return render(request, 'index.html')


def exibir_perfil(request, perfil_id):
    perfil = Perfil()
    if(perfil_id == '1'):
        perfil = Perfil('Teste Nome', 'teste@teste.com', '2312313', 'Teste Ltda')


    context = {
        'perfil':perfil
    }
    return render(request=request, template_name='perfil.html', context=context)
