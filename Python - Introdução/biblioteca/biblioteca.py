import re

def ger_nome_convite(nome):
    posicao_final = len(nome)
    posicao_inicial = posicao_final-4

    parte1 = nome[0:4]
    parte2 = nome[posicao_inicial:posicao_final]
    return ('{} {}'.format(parte1,parte2))


def envia_convite(nome_formatado):
    print('Enviando convite para {}'.format(nome_formatado))


def processa_convite(nome):
    return envia_convite(ger_nome_convite(nome))


def cadastrar(nomes):
    print('Digite o nome:')
    nome = input()
    nomes.append(nome)
    return nomes

def remover(nomes):
    print('Qual nome gostaria de remover?')
    nome = input()
    nomes.remove(nome)
    return nomes


def listar_nomes(nomes):
    print('Listando nomes:')
    for each_nome in nomes:
        print(each_nome)


def alterar_nome(nomes):
    print('Qual nome gostaria de alterar?')
    nome = input()
    if(nome in nomes):
        print('Digite o novo nome:')
        novo_nome = input()
        indice = nomes.index(nome)
        nomes[indice] = novo_nome
    else:
        print('Nome não encontrado!!!')
    return nomes


def procurar_nome(nomes):
    print('Qual nome desja procurar?')
    nome = input()
    if(nome in nomes):
        print('nome encontrado: {}\n posição de num: {}'.format(nome, nomes.index(nome)))
    else:
        print('Nome {}, não encontrado'.format(nome))


def procurar_nomes_regex(nomes):
    print('Digite o nome que vc deseja procurar')
    regex = input()
    achado = ''
    for nome in nomes:
        if re.findall(regex, nome):
            print(nome)
