from unicodedata import normalize
from pprint import pprint
import operator

opc = {'sair': [0, 0, 'Sair do sistema.'], 'openFile': [0, 1, 'Abrir um arquivo.'], 'printTexto': [1, 2, 'Printar o texto original.'], 'limpaTexto': [1, 3, 'Remove a acentuação e caracteres especiais do texto.'], 'printTextoForm': [2, 4, 'Printar o texto formatado.'], 'contaPalavras': [2, 5, 'Contar o número de aparições das palavras.'], 'printContagem': [3, 6, 'Mostrar a quantidade de vezes que cada palavra apareceu.'], 'query': [3, 7, 'Pesquisas a quantidade de vezes que determinada(s) palavra(s) aparece(m) no texto.'], 'printExtremos': [3, 8, 'Mostrar as palavras mais e menos repetidas no texto.'], 'mapLetras': [3, 9, 'Contar as letras de cada palavra(map)'], 'printMap': [4, 10, 'Mostrar a quantidade de repetições de cada letra por palavra(map)'], 'combineLetras': [4, 11, 'Agrupar as letras(combine)'], 'printCombine': [5, 12, 'Mostrar os grupos de letras(combine)'], 'reduceLetras': [5, 13, 'Fazer a contagem das letras(reduce)'], 'printReduce': [6, 14, 'Mostrar a contagem de letas (reduce)']}

texto = ''
textoForm = ''
priv = 0

def openFile():
    while True:
        try:
            fileName = input('Digite o nome do arquivo txt que vocé deseja abrir (sem a extensão do arquivo): ')
            with open(f'./{fileName}.txt', 'r', encoding='utf-8') as arquivo:
                global texto
                texto = arquivo.read()
            break
        except:
            print('\nPoxa bicho, escreve que nem gente, com todo o respeito... Pai não sabe o que é esse arquivo. Tenta de novo ai.\n')
    global priv
    priv = 1

def printTexto():
    global texto
    print(texto)

def limpaTexto():
    global texto, textoForm
    textoForm = normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8').lower()
    global priv
    priv = 2

def printTextoForm():
    global textoForm
    print(textoForm)

def contaPalavras():
    global textoForm
    arrayTexto = textoForm.split(' ')
    contagem = dict()
    for i in arrayTexto:
        if i not in list(contagem.keys()):
            contagem[i] = arrayTexto.count(i)
    global contagemDec
    contagemDec = dict(sorted(contagem.items(), key=operator.itemgetter(1), reverse=True))
    global priv
    priv = 3

def printContagem():
    global contagemDec
    for k, v in contagemDec.items():
        print(f'{k} = {v}')

def query():
    pedido = input('Digite a(s) palavra(s) que deseja saber a quantidade de aparicão(ões) no texto (separadas por virgula): ')
    pedidos = pedido.split(',')
    print()
    for i in pedidos:
        i = i.strip()
        try:
            print(f'{i} = {contagemDec[i]}')
        except:
            print(f'\nPoxa bicho, escreve que nem gente, com todo o respeito... Pai não sabe o que é {i}\n')
            query()

def printExtremos():
    minimos = [k for k, v in contagemDec.items() if v == contagemDec[min(contagemDec, key=contagemDec.get)]]
    maximos = [k for k, v in contagemDec.items() if v == contagemDec[max(contagemDec, key=contagemDec.get)]]
    
    if len(minimos) <= 1:
        print(f'A palavra que menos apareceu foi -> "{min(contagemDec, key=contagemDec.get)}" com apenas {contagemDec[min(contagemDec, key=contagemDec.get)]} aparições.')
    else:
        todosMinimos = ''
        for i in range(len(minimos)):
            todosMinimos += '"' + minimos[i] + '"' + ',' if i != len(minimos) - 1 else ''

        print(f'As palavras que menos apareceram foram -> {todosMinimos} com apenas {contagemDec[min(contagemDec, key=contagemDec.get)]} aparições.')

    print()

    if len(maximos) <= 1:
        print(f'A palavra que mais apareceu foi -> "{max(contagemDec, key=contagemDec.get)}" com {contagemDec[max(contagemDec, key=contagemDec.get)]} aparições.')
    else:
        todosMaximos = ''
        for i in range(len(maximos)):
            todosMaximos += '"' + maximos[i] + '"' + ',' if i != len(maximos) - 1 else ''

        print(f'As palavras que mais apareceram foram -> {todosMaximos} com {contagemDec[max(contagemDec, key=contagemDec.get)]} aparições.')

def mapLetras():
    global contagemDec, letraPalavra
    letraPalavra = []
    i = 0
    for k, v in contagemDec.items():
        letraPalavra.append([k, []])
        for l in k:
            letraPalavra[i][1].append([l, 1])
        i += 1
    global priv
    priv = 4

def printMap():
    global letraPalavra
    for i in letraPalavra:
        print(f'{i[0]}:')
        pprint(i[1])
        print()

def combineLetras():
    global letraPalavra, letraGrupo
    letraGrupo = []
    jaFoi = []
    ind = 0
    for i in letraPalavra:
        for j in i[1]:
            if j[0] in jaFoi:
                continue
            letraGrupo.append([])
            for k in letraPalavra:
                for l in k[1]:
                    if j[0] == l[0]:
                        letraGrupo[ind].append(j)
            jaFoi.append(j[0])
            ind += 1
    global priv
    priv = 5

def printCombine():
    global letraGrupo
    for i in letraGrupo:
        print(f'{i[0][0]}:')
        pprint(i)
        print()

def reduceLetras():
    global letraGrupo, letraReduced
    letraReduced = []
    for i in letraGrupo:
        letraReduced.append([i[0][0], len(i)])
    global priv
    priv = 6

def printReduce():
    global letraReduced
    for i in letraReduced:
        print(f'{i[0]}: {i[1]}')
    print()
    
def sair():
    exit()

sel = -1
while sel != 0:
    print()
    for k, v in opc.items():
        if priv >= v[0]:
            print(f'{v[1]} - {v[2]}')
    
    sel = int(input('\nDigite a opção que deseja: '))
    print()

    for k, v in opc.items():
        if sel == v[1]:
            if priv >= v[0]:
                exec(f'{k}()')
                break
            else:
                print('Infelizmente você não possui os pré-requisitos para realizar essa ação, favor realizar as ações anteriores primeiro.')
                break
    else:
        print('Essa função não existe. Tente novamente...')

