

from datetime import date

class Nota_fiscal(object):

    def __init__(self,razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes=''):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__itens = itens
        self.__data_de_emissao = data_de_emissao
        self.__detalhes = detalhes

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes

    @property
    def razao_social(self):
        return self.__razao_social



if __name__ == '__main__':
    from Python_Design_Partterns.Builder.orcamento import Item
    from Python_Design_Partterns.Builder.criador_nota_fiscal import Criador_nota_fiscal
    itens =[
        Item(nome='ITEM-A',valor=100),
        Item(nome='ITEM-B', valor=200)
    ]

    nota_fiscal = Criador_nota_fiscal().com_cnpj('2131313131').com_itens(itens).com_razao_social('Teste').constroi()
    print(nota_fiscal.data_de_emissao)