
class Perfil(object):
    """Classe padrão para perfis de usuário"""

    def __init__(self, nome, telefone, empresa):
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
        arquivo = open(nome_arquivo, 'r')
        perfis =[]
        for each_linha in arquivo:
            split = each_linha.split(',')
            perfis.append(classe(split[0], split[1], split[2]))
        arquivo.close()
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
