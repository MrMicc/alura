from django.shortcuts import render
from perfis.models import Perfil

# Create your views here.

def index(request):
    """Delcaração de função de view"""
    context = {
        'perfis': Perfil.objects.all(),
        'perfil_logado': get_perfil_logado(request)
    }

    return render(request, 'index.html', context=context)


def exibir_perfil(request, perfil_id):

    perfil = Perfil.objects.get(id=perfil_id)

    context = {
        'perfil':perfil
    }
    return render(request=request, template_name='perfil.html', context=context)


def exibir_perfis(request):
    context = {'perfis': Perfil.objects.all()}
    return render(request=request, template_name='lista_perfis.html', context=context)

def convidar_perfil(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return index(request=request)

def get_perfil_logado(request):
    #TODO alterar para pegar o perfil de fato logado e não default 1
    return Perfil.objects.get(id=5)