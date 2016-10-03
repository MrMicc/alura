class Soma(object):
    def __init__(self, expressao_esquerda, expressao_direta):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direta = expressao_direta

    @property
    def avalia(self):
        return Numero(self.__expressao_esquerda.avalia() + self.__expressao_direta.avalia())


class Subtracao(object):
    def __init__(self, expressao_esquerda, expressao_direta):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direta = expressao_direta

    @property
    def avalia(self):
        return Numero(self.__expressao_esquerda.avalia() - self.__expressao_direta.avalia())


class Numero(object):
    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero

    def __str__(self):
        return '{}'.format(self.__numero)


if __name__ == '__main__':
    expressao_direita = Soma(Numero(10), Numero(20))
    expressao_esquerda = Subtracao(Numero(20),Numero (10))
    print('{}+{}'.format(expressao_direita.avalia, expressao_esquerda.avalia))
    print('{}'.format(Soma(expressao_direita.avalia, expressao_esquerda.avalia).avalia))