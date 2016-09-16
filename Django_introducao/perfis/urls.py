"""Django_introducao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from perfis import views


#^inicio da String
#fim da da String$
#logo ser quisermos uma url especifica ^STRING$
#\d+ -> 1 ou mais digitos
#grupos -> (?P<variavel>EXPREGULAR)
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$',views.exibir_perfil, name='perfis'), #url de um perfil especifico
    url(r'^perfis$',views.exibir_perfis, name='lista_todos_perfis'),

]
