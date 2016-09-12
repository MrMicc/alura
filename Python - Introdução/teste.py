from biblioteca.models import Perfil
from biblioteca.models import Data
from biblioteca.models import Pessoa
from biblioteca.models import Perfil_Vip

if __name__ == '__main__':


    perfis =[]
    perfis.append(Perfil('teste da silva sauro', '2345678', 'desempregado'))
    perfis.append(Perfil_Vip('João da Silva', 'nao tenho', 'super bem empregado',apelido='doidao'))

    for each_perfil in perfis:
        print (each_perfil)
        print('---------')
        print(each_perfil.get_dictionary())
        print('##################')
        each_perfil.set_curtir()
        print(each_perfil)
        print('\n++++++++++\n\n')


#    data = Data(12,10,2015)
#    print(data)

#    pessoa = Pessoa("Ronaldo", 70, 1.70)
#    print(pessoa.get_imc())




