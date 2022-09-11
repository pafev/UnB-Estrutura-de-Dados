def constituiArvoreBinariaDeBusca(raiz):
    validade = True
    if raiz:
        if raiz.esq:
            if raiz.esq > raiz.dado:
                validade = False
                return validade
            validade = constituiArvoreBinariaDeBusca(raiz.esq)
        if raiz.dir:
            if raiz.dir < raiz.dado:
                validade = False
                return validade
            validade = constituiArvoreBinariaDeBusca(raiz.dir)
    return validade