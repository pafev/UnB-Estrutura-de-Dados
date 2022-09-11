tamanhoCaminhos = []
temp = 0
temp3 = 0

def mostra2(arvore, prefix):
    global temp3
    if arvore.dado:
        print(temp*prefix + f'{arvore.dado}')
    for filho in arvore.filhos:
        temp3 += 1
        mostra2(filho, prefix)
        temp3 -= 1

def mostra(arvore, prefix):
    global temp3
    if arvore.dado:
        print(temp*prefix + f'{arvore.dado}')
    for filho in arvore.filhos:
        temp3 += 1
        mostra2(filho, prefix)
        temp3 -= 1
    temp3 = 0

def mostra_arvore_e_nivel2(raiz):
    global tamanhoCaminhos
    global temp
    if raiz.dado:
        if raiz.dir:
            temp += 1
            mostra_arvore_e_nivel2(raiz.dir)
            temp -= 1
        if raiz.esq:
            temp += 1
            mostra_arvore_e_nivel2(raiz.esq)
            temp -= 1
        temp2 = temp
        tamanhoCaminhos.append(temp2)
        del temp2


def mostra_arvore_e_nivel(raiz, value):
    mostra(raiz, '__')
    global tamanhoCaminhos
    global temp
    if raiz:
        if raiz.dir:
            temp += 1
            mostra_arvore_e_nivel2(raiz.dir)
            temp -= 1
        if raiz.esq:
            temp += 1
            mostra_arvore_e_nivel2(raiz.esq)
            temp -= 1
        temp2 = temp
        tamanhoCaminhos.append(temp2)
        del temp2
    print(max(tamanhoCaminhos))
    tamanhoCaminhos = []
    temp = 0