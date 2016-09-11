
class Perfil(object):
    'Classe padrão para perfis de usuário'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome;
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def get_dictionary(self):
        return {'nome':self.nome, 'telefone': self.telefone, 'empresa': self.empresa, 'curtidas': self.__curtidas}

    def set_curtir(self):
        self.__curtidas+=1

    def get_curtidas(self):
        return self.__curtidas

    def __str__(self):
        return ('nome: {}\ntelefone: {}\n empresa:{},\ncurtidas: {}'.format(self.nome, self.telefone, self.empresa, self.__curtidas))


class Data(object):
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return '{}/{}/{}'.format(self.dia,self.mes,self.ano)


class Pessoa(object):
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.__imc = 0

    def get_imc(self):
        self.__imc = self.peso/self.altura**2
        return 'IMC do {} é de: {}'.format(self.nome, self.__imc)
