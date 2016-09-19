from django.shortcuts import render
from perfis.models import Perfil, Convite
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

# Create your views here.

@login_required
def index(request):
    """Delcaração de função de view"""
    print(request.user.username)  # novo
    print(request.user.email)  # novo
    print(request.user.has_perm('perfis.add_convite'))  # novo

    context = {
        'perfis': Perfil.objects.all(),
        'perfil_logado': get_perfil_logado(request)
    }

    return render(request, 'perfil/index.html', context=context)

@login_required
def exibir_perfil(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)

    ja_eh_contato= perfil in perfil_logado.contatos.all()


    context = {
        'perfil':perfil,
        'perfil_logado': get_perfil_logado(request),
        'ja_eh_contato':ja_eh_contato
    }
    return render(request=request, template_name='perfil/perfil.html', context=context)


@login_required
def exibir_perfis(request):
    context = {
        'perfis': Perfil.objects.all(),
        'perfil_logado': get_perfil_logado(request)}
    return render(request=request, template_name='perfil/lista_perfis.html', context=context)


@login_required
def convidar_perfil(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return index(request=request)


@login_required
def aceitar(request, id_convite):
    convite = Convite.objects.get(id=id_convite)
    convite.aceitar()
    return index(request)

@login_required
def get_perfil_logado(request):
    return request.user.perfil