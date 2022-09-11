filaPrioridades = [[],[],[],[],[],[]]

def addProcesso():
    solicitacao = input()
    P = int(solicitacao[0])
    processo = solicitacao[2:]
    filaPrioridades[P].append(processo)


def scramble(caracteres):
    resultado = []
    resultado_aux = []
    inicio = False
    while caracteres:
        if caracteres[0] != '(' and caracteres[0] != ')':
            if inicio:
                while caracteres and caracteres[0] != '(' and caracteres[0] != ')':
                    resultado_aux.append(caracteres.pop(0))
                resultado = resultado_aux + resultado
                resultado_aux = []
                inicio = False
            elif not inicio:
                resultado.append(caracteres.pop(0))
        elif caracteres[0] == '(':
            inicio = True
            caracteres.pop(0)
        elif caracteres[0] == ')':
            inicio = False
            caracteres.pop(0)
    return resultado


def dekey(numeros):
    O = int(numeros.split()[0])
    S = numeros.split()[1:]
    count = 0
    while count < O:
        A = S.pop(0)
        B = S.pop(0)
        if int(A) < int(B):
            S.append(A)
            S.insert(0, B)
        else:
            S.insert(0, A)
            S.append(B)
        count += 1
    return S


def imprimeResultado(resultado):
    for i in range(len(resultado)):
        print(resultado[i], end = '')
    print()


def executaProxComando():
    for processos in filaPrioridades:
        if processos:
            aExecutar = processos.pop(0)
            if aExecutar[0:8] == 'scramble':
                caracteres = list(aExecutar[9:])
                resultado = scramble(caracteres)
                if resultado:
                    imprimeResultado(resultado)
            elif aExecutar[0:5] == 'dekey':
                resultado = dekey(aExecutar[6:])
                imprimeResultado(resultado)
            break


def mostraProcessosOrfaos():
    qtd = 0
    for processos in filaPrioridades:
        qtd += len(processos)
    print(f'{qtd} processo(s) órfão(s).')


while True:
    comando = input()
    if comando.split()[0] == 'enqueue':
        X = int(comando.split()[1])
        count = 0
        while count < X:
            addProcesso()
            count += 1
    elif comando == 'stop':
        mostraProcessosOrfaos()
        break
    elif comando == 'go':
        executaProxComando()