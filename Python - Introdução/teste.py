from biblioteca.models import Perfil
from biblioteca.models import Data
from biblioteca.models import Pessoa

if __name__ == '__main__':

    perfis =[]
    perfis.append(Perfil('teste da silva sauro', '2345678', 'desempregado'))
    perfis.append(Perfil('João da Silva', 'nao tenho', 'super bem empregado'))

    for each_perfil in perfis:
        print (each_perfil)
        print('---------')
        print(each_perfil.get_dictionary())
        print('##################')


    data = Data(12,10,2015)
    print(data)

    pessoa = Pessoa("Ronaldo", 70, 1.70)
    print(pessoa.get_imc())

