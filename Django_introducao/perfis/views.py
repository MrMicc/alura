from django.shortcuts import render
from perfis.models import Perfil, Convite

# Create your views here.

def index(request):
    """Delcaração de função de view"""
    context = {
        'perfis': Perfil.objects.all(),
        'perfil_logado': get_perfil_logado(request)
    }

    return render(request, 'perfil/index.html', context=context)


def exibir_perfil(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)

    ja_eh_contato= perfil in perfil_logado.contatos.all()


    context = {
        'perfil':perfil,
        'ja_eh_contato':ja_eh_contato
    }
    return render(request=request, template_name='perfil/perfil.html', context=context)


def exibir_perfis(request):
    context = {'perfis': Perfil.objects.all()}
    return render(request=request, template_name='perfil/lista_perfis.html', context=context)

def convidar_perfil(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return index(request=request)


def aceitar(request, id_convite):
    convite = Convite.objects.get(id=id_convite)
    convite.aceitar()
    return index(request)


def get_perfil_logado(request):
    #TODO alterar para pegar o perfil de fato logado e não default 1
    return Perfil.objects.get(id=1)