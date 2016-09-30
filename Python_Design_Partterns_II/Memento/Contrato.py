class Contrato(object):
    def __init__(self, nome, data, tipo=None):
        self.__nome = nome
        self.__data = data
        if (tipo is None):
            self.__tipo = Novo()
        else:
            self.__tipo = tipo
        self.historico = Historico()

    def avança(self):
        if (type(self.tipo) is type(Novo())):
            self.historico.salva_historico(Contrato(nome=self.nome, data=self.data, tipo=self.__tipo))
            self.__tipo = Em_andamento()
        elif(type(self.__tipo) is type(Em_andamento()) ):
            self.__tipo = Acerdato()
        elif(type(self.__tipo) is type(Acerdato())):
            self.__tipo = Concluido()

    @property
    def nome(self):
        return self.__nome

    @property
    def data(self):
        return self.__data

    @property
    def tipo(self):
        return self.__tipo



class Historico(object):
    def __init__(self):
        self.__contratos = []

    def salva_historico(self, contrato):
        self.__contratos.append(contrato)

    def get_historico(self, indice):
        return self.__contratos[indice]


class Novo(object):
    def __str__(self):
        return 'NOVO'

class Em_andamento(object):
    def __str__(self):
        return 'EM ANDAMENTO'

class Acerdato(object):
    def __str__(self):
        return 'ACERTADO'

class Concluido(object):
    def __str__(self):
        return 'CONCLUIDO'



if __name__ == '__main__':
    from datetime import date

    contrato = Contrato(nome='Teste', data=date.today())

    print('{} - {}'.format(contrato.nome, contrato.tipo))

    contrato.avança()
    print('{} - {}'.format(contrato.nome, contrato.tipo))
    print('Historico {} - {}'.format(contrato.historico.get_historico(0).nome, contrato.historico.get_historico(0).tipo))