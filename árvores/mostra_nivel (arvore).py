def mostra2(raiz):
    if raiz.esq == None and raiz.dir == None:
        return f'({raiz.dado} () ())'
    elif raiz.esq != None and raiz.dir == None:
        return f'({raiz.dado} {mostra2(raiz.esq)} ())'
    elif raiz.esq == None and raiz.dir != None:
        return f'({raiz.dado} () {mostra2(raiz.dir)})'
    elif raiz.esq != None and raiz.dir != None:
        return f'({raiz.dado} {mostra2(raiz.esq)} {mostra2(raiz.dir)})'

def mostra(raiz):
    if raiz.esq == None and raiz.dir == None:
        print(f'({raiz.dado} () ())')
    elif raiz.esq != None and raiz.dir == None:
        print(f'({raiz.dado} {mostra2(raiz.esq)} ())')
    elif raiz.esq == None and raiz.dir != None:
        print(f'({raiz.dado} () {mostra2(raiz.dir)})')
    elif raiz.esq != None and raiz.dir != None:
        print(f'({raiz.dado} {mostra2(raiz.esq)} {mostra2(raiz.dir)})')

def mostra_nivel(raiz, nivel):
    if nivel == 0:
        if raiz:
            mostra(raiz)
    else:
        if raiz.esq:
            mostra_nivel(raiz.esq, nivel - 1)
        if raiz.dir:
            mostra_nivel(raiz.dir, nivel - 1)