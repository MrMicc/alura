

from datetime import date

class Nota_fiscal(object):

    def __init__(self,razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes=''):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__itens = itens
        self.__data_de_emissao = data_de_emissao
        self.__detalhes = self.__tamanho_detalhe(detalhes)

        self.__imprimir()
        self.__envia_por_email()
        self.__salva_no_banco()


    def __imprimir(self):
        print('Imprimindo a nota fistal:{}'.format(self.__razao_social))

    def __envia_por_email(self):
        print('Enviando por mail: {}'.format(self.__razao_social))

    def __salva_no_banco(self):
        print('Salvando no banco: {}'.format(self.razao_social))

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
    itens =[
        Item(nome='ITEM-A',valor=100),
        Item(nome='ITEM-B', valor=200)
    ]


    nota_fiscal = Criador_nota_fiscal().com_cnpj('2131313131').com_itens(itens).com_razao_social('Teste').com_detalhes('adasdad').constroi()
    print(nota_fiscal.data_de_emissao)