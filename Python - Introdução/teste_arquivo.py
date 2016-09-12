from biblioteca.models import Perfil

if __name__ == '__main__':
    arquivo = open('./arquivos/perfis.csv', 'r')
    for each_linha in arquivo:
        print(each_linha)

    arquivo.close()

    arquivo = open('./arquivos/arquivo_novo.csv', 'w')
    arquivo.write('Pedro da silva, 21-9887897, Super Amigos\n')
    arquivo.close()

    logo = open('./arquivos/python-logo.png', 'rb')
    data = logo.read() # lendo conteudo binario
    logo.close()

    #inserindo os dados iguais
    logo2 = open('./arquivos/python-logo2.png', 'wb')
    logo2.write(data)
    logo2.close()