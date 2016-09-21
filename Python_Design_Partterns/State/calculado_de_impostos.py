from Python_Design_Partterns.State.orcamento import Orcamento, Item
from Python_Design_Partterns.State.impostos import ICMS, ISS,ICPP,IKCV


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ == '__main__':

    calculador = Calculador_de_impostos()
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM-1', 100))
    orcamento.adiciona_item(Item('ITEM-2', 50))
    orcamento.adiciona_item(Item('ITEM-3', 400))

    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print('ICPP e KCV')
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())

    print('Impostoso Compostos')
    calculador.realiza_calculo(orcamento, ICPP(IKCV()))
