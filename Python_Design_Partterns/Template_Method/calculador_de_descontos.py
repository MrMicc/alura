# -*- coding: UTF-8 -*-
from Python_Design_Partterns.Template_Method.descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Desconto_zerado

class Calculador_de_descontos(object):
    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_itens(Desconto_por_mais_de_quinhentos_reais(
            Desconto_zerado()
            )
        ).calcula(orcamento)

        return desconto


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