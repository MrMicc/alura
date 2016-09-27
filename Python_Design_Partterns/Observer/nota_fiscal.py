from datetime import date

class Nota_fiscal(object):

    def __init__(self,razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes='', observadores=[]):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__itens = itens
        self.__data_de_emissao = data_de_emissao
        self.__detalhes = self.__tamanho_detalhe(detalhes)

        #observer
        for each_observador in observadores:
            each_observador(self)


    def __tamanho_detalhe(self, detalhes):
        if(len(detalhes)>20):
            raise Exception('Detalhe Muito Extenso')
        else:
            return detalhes

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
    from Python_Design_Partterns.Observer.observadores import imprimir, envia_por_email, salva_no_banco
    itens =[
        Item(nome='ITEM-A',valor=100),
        Item(nome='ITEM-B', valor=200)
    ]


    nota_fiscal = Nota_fiscal(
        razao_social='Teste LTDA',
        cnpj='12313123123131231',
        itens=itens,
        detalhes='dasdadad',
        observadores=[imprimir, salva_no_banco, salva_no_banco, envia_por_email]
    )
    print(nota_fiscal.data_de_emissao)