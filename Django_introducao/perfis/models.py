from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#como herdamos um model não precisamos da funciton init
#ao final da alteração de um model é necessário rodar o makemigrations
#2 - Aplicar o schema no banco migrate
class Perfil(models.Model):

    nome = models.CharField(max_length=255, null=False)
    #email = models.EmailField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=155, null=False)
    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User, related_name='perfil')

    #delegando para utilizar o email do User
    @property
    def email(self):
        return self.usuario.email



    def convidar(self, perfil_convidado):
        '''Viabiliza um Perfil logado na seção a realizar um convite um Perfil não logado'''
        convite = Convite(solicitante=self, convidado=perfil_convidado)
        convite.save()


class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')
    #Para buscar os convidados via Query == Convite.objects.filter(convidado__id = 1)

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante) #addicionando no objeto do perfil convidado o contato do solicitante
        self.solicitante.contatos.add(self.convidado) #add no objeto do solicitante o contato do convidado no perfil do solicitante
        self.delete() #apagando o convite




