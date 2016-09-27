from Python_Design_Partterns.Observer.orcamento import Orcamento
from Python_Design_Partterns.Observer.impostos import ICMS, ISS


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ == '__main__':

    calculador = Calculador_de_impostos()
    orcamento = Orcamento(500)

    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())