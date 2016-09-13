import sys
class Perfil(object):
    """Classe padrão para perfis de usuário"""

    def __init__(self, nome, telefone, empresa):
        if (len(nome) < 3 or nome is None) or (len(empresa) < 3 or empresa is None):
            raise ArgumentoInvalidoError('o parametro nome e empresa tem que ter ao menos 3 caracteres!!!')
        if(len(telefone) < 10):
            raise ArgumentoInvalidoError('O parametro telefone tem que ter ao menos 3 caracteres!!!')
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def get_dictionary(self):
        return {'nome':self.nome, 'telefone': self.telefone, 'empresa': self.empresa, 'curtidas': self.get_curtidas()}

    def set_curtir(self):
        self.__curtidas+=1

    def get_curtidas(self):
        return self.__curtidas

    #@staticmethod
    @classmethod
    def gerar_perfis(classe, nome_arquivo):

        perfis = []
        try:
            with open(nome_arquivo, 'r') as arquivo:
                for each_linha in arquivo:
                    split = each_linha.split(',')
                    if(len(split) < 3 or len(split) > 4):
                        raise PerfilError('A linha "{}", está fora do padrão esperado!!!'.format(each_linha))
                        raise V

                    perfis.append(classe(split[0], split[1], split[2]))
        except IOError as error:
            print('IOError:: algum problema ocorreu no arquivo: {}'.format(nome_arquivo), file=sys.stderr)
        return perfis

    def __str__(self):
        return ('nome: {}\ntelefone: {}\n empresa:{}'.format(self.nome, self.telefone, self.empresa, self.get_curtidas()))


class Perfil_Vip(Perfil):
    """Classe padrão para perfis de usuário VIPs"""

    def __init__(self, nome, telefone, empresa, apelido=''):
        #Chamando o construtor do pai
        super(Perfil_Vip, self).__init__(nome=nome, telefone=telefone, empresa=empresa)
        self.apelido = apelido

    def get_creditos(self):
        """Para cada curtida realizada em um vip, existe um credito de 10reais"""
        return self.get_curtidas() * 10.0

    def get_dictionary(self):
        return {'nome':self.nome,'apelido':self.apelido, 'telefone': self.telefone, 'empresa': self.empresa, 'curtidas': self.get_curtidas(), 'creditos:': self.get_creditos()}

    def __str__(self):
        return ('nome: {}\napelido: {}\ntelefone: {}\n empresa:{},\ncurtidas: {}\n creditos: {}'.format(self.nome, self.apelido,self.telefone, self.empresa, self.get_curtidas(), self.get_creditos()))


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


class ArgumentoInvalidoError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __srt__(self):
        return repr(self.msg)

class PerfilError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
