class Orcamento(object):

    def __init__(self, valor):
        self.__valor = valor #atributo "privado"


    @property
    def valor(self):
        return self.__valor