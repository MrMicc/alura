from abc import ABCMeta, abstractmethod

class Template_de_imposto_condicional(object):

    __metaclass = ABCMeta

    def calcula(self,orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self,orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self,orcamento):
        pass


class ISS(object):
    def calcula(self, orcamento):
        return orcamento.valor*0.1


class ICMS(object):
    def calcula(self, orcamento):
        return orcamento.valor*0.06


class ICPP(Template_de_imposto_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):
      if orcamento.valor > 500:
          return True
      else:
          return False

    def maxima_taxacao(self, orcamento):
        return orcamento.valor*0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor*0.05



class IKCV(Template_de_imposto_condicional):

    def __item_item_maior_que_100_reais(self,orcamento):
        for each_item in orcamento.get_itens:
            if each_item.valor > 100:
                return True
        return False

    def deve_usar_maxima_taxacao(self, orcamento):
        if(orcamento.valor > 500 and self.__item_item_maior_que_100_reais(orcamento)):
            return True
        else:
            return False
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

