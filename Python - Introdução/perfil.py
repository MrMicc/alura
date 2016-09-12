from biblioteca.models import Perfil
from biblioteca.models import Perfil_Vip


def carrega_arquivo():
    for each_perfil in Perfil.gerar_perfis('./arquivos/perfis.csv'):
        print(each_perfil)
        print(type(each_perfil))

    for each_perfil_vip  in Perfil_Vip.gerar_perfis('./arquivos/perfis.csv'):
        print(each_perfil_vip)
        print(type(each_perfil_vip))

carrega_arquivo()