from django.shortcuts import render
from perfis.models import Perfil

# Create your views here.

def index(request):
    """Delcaração de função de view"""
    context = {
        'perfis': Perfil.objects.all()
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