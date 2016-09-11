# -*- coding: UTF-8 -*-
from biblioteca import biblioteca as bl


def menu():
    nomes = []
    escolha = -1
    while(escolha != 0):
        print('Digte: \n"1" - Cadastrar nomes;\n"2" - Remover nomes;\n"3" - Listar nomes\n"4" - Alterar nome\n"5" - '
              'Procurar nomes;\n"6" - Pocurar Tudo;\n0" - Sair')
        escolha = int(input())
        if(escolha==1):
            bl.cadastrar(nomes)

        elif(escolha==2):
            bl.remover(nomes)

        elif(escolha==3):
            bl.listar_nomes(nomes)
        elif(escolha==4):
            bl.alterar_nome(nomes)
        elif(escolha==5):
            bl.procurar_nome(nomes)
        elif(escolha==6):
            bl.procurar_nomes_regex(nomes)




menu()