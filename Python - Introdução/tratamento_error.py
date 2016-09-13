from biblioteca.models import Perfil
def tratamento_error():
    perfis = Perfil.gerar_perfis('./arquivos/perfis2.csv')
    for each_perfil in perfis:
        print(each_perfil)




tratamento_error()