
class Perfil(object):
    'Classe padrão para perfis de usuário'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome;
        self.telefone = telefone
        self.empresa = empresa

    def get_dictionary(self):
        return {'nome':self.nome, 'telefone': self.telefone, 'empresa': self.empresa}

    def __str__(self):
        return ('nome: {}\ntelefone: {}\n empresa:{}'.format(self.nome, self.telefone, self.empresa))


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

    def get_imc(self):
        imc = self.peso/self.altura**2
        return 'IMC do {} é de: {}'.format(self.nome, imc)
