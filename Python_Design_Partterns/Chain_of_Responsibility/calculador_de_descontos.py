# -*- coding: UTF-8 -*-

class Calculador_de_descontos(object):
    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            print(orcamento.valor*0.1)

        elif orcamento.valor > 500:
            return orcamento.valor*0.07



if __name__ == '__main__':
    from Python_Design_Partterns.Chain_of_Responsibility.orcamento import Orcamento, Item
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM-1',100))
    orcamento.adiciona_item(Item('ITEM-2', 50))
    orcamento.adiciona_item(Item('ITEM-3', 400))

    print(orcamento.valor)

    calculador = Calculador_de_descontos()
    desconto_calculador = calculador.calcula(orcamento)
    print('Desconto: {}'.format(desconto_calculador))