from abc import ABCMeta, abstractmethod

class Estado_de_orcamento(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass




class Em_aprovacao(Estado_de_orcamento):
    def finaliza(self, orcamento):
        raise Exception('Orcameno em aprovacao nao pode ir para finalizado')

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

class Aprovado(Estado_de_orcamento):
    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

    def reprova(self, orcamento):
        raise Exception('Orcamento aprovados nao pode ser reprovado!!')

    def aprova(self, orcamento):
        raise Exception('Orcamento já aprovado!!')

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor*0.05)


class Reprovado(Estado_de_orcamento):
    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

    def reprova(self, orcamento):
        raise Exception('Orcamento reprovado nao pode ser Reprovado')

    def aprova(self, orcamento):
        raise Exception('Orcamento reprovado nao pode ser Aprovado')


    def aplica_desconto_extra(self, orcamento):
        raise (Exception('Orcamento reprovado não possui desconto extra!!!'))


class Finalizado(Estado_de_orcamento):
    def finaliza(self, orcamento):
        raise Exception('Orcamento já finalizado!!!')

    def reprova(self, orcamento):
        raise Exception('Orcamento já finalizado!!!')

    def aprova(self, orcamento):
        raise Exception('Orcamento já finalizado!!!')

    def aplica_desconto_extra(self, orcamento):
        raise (Exception('Orcamento finalizado, não é possivel dar desconto extra!!!'))


class Orcamento(object):


    def __init__(self):
        self.__itens = []
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0

    def aplica_desconto(self):
        self.estado_atual.aplica_desconto_extra(self)

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra = desconto

    @property
    def valor(self):
        total = 0.0
        for each_item in self.__itens:
            total += each_item.valor
        return total - self.__desconto_extra

    @property
    def get_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)


class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor


if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM-1', 100))
    orcamento.adiciona_item(Item('ITEM-2', 50))
    orcamento.adiciona_item(Item('ITEM-3', 400))

    print(orcamento.valor)
    #orcamento.estado_atual.aplica_desconto_extra(orcamento)
    print(orcamento.valor)
    orcamento.aprova()
    orcamento.aplica_desconto()
    print(orcamento.valor)

