temp = 0
temp2 = 0

class tree():
    def __init__(self, data):
        self.dado = data
        self.childs = []
        self.prob = 0.0

def probtree2(arvore):
    global temp2
    if arvore:
        print(temp2*'..' + f'{arvore.dado[0]}' + f' ({arvore.prob:.2f}%)')
        for child in arvore.childs:
            temp2 += 1
            probtree2(child)
            temp2 -= 1

def probtree(arvore):
    global temp2
    if arvore:
        print(temp2*'..' + f'{arvore.dado[0]}' + f' ({arvore.prob:.2f}%)')
        for child in arvore.childs:
            temp2 += 1
            probtree2(child)
            temp2 -= 1
    temp2 = 0

def gametree2(arvore):
    global temp
    if arvore:
        print(temp*'__' + f'{arvore.dado[0]}')
        for child in arvore.childs:
            temp += 1
            gametree2(child)
            temp -= 1

def gametree(arvore):
    global temp
    if arvore:
        print(temp*'__' + f'{arvore.dado[0]}')
        for child in arvore.childs:
            temp += 1
            gametree2(child)
            temp -= 1
    temp = 0

def addOneChild(raiz):
    newChild = tuple(input().split())
    newChildTree = tree(newChild)
    if newChild[0] == 'V':
            newChildTree.prob = 100.0
    raiz.childs.append(newChildTree)

def addMoreChild2(arvore):
    for child in arvore.childs:
        if child.dado[0] == '?':
            for _ in range(int(child.dado[1])):
                addOneChild(child)

def addMoreChild(arvore):
    for child in arvore.childs:
        if child.dado[0] == '?':
            for _ in range(int(child.dado[1])):
                addOneChild(child)
    for child in arvore.childs:
        addMoreChild2(child)
    for child in arvore.childs:
        for grandson in child.childs:
            addMoreChild(grandson)

def defineProb(arvore, prob_total, qtd_folhas):
    if arvore.childs:
        for child in arvore.childs:
            if child.dado[0] in 'VED':
                prob_total += defineProb(child, 0, 0)
                qtd_folhas += 1
            elif child.dado[0] == '?':
                prob_temp, qtd_folhas_temp = defineProb(child, 0, 0)
                prob_total += prob_temp
                qtd_folhas += qtd_folhas_temp
            arvore.prob += child.prob
        arvore.prob = prob_total / qtd_folhas
        return prob_total, qtd_folhas
    else:
        return arvore.prob

arvore = tree(None)

while True:
    comando = input()
    if comando == 'gametree':
        gametree(arvore)
        break
    elif comando == 'probtree':
        defineProb(arvore, 0, 0)
        probtree(arvore)
        break
    else:
        data = tuple(comando.split())
        arvore  = tree(data)
        if arvore.dado[0] == '?':
            for _ in range(int(arvore.dado[1])):
                addOneChild(arvore)
            addMoreChild(arvore)
        elif arvore.dado[0] == 'V':
            arvore.prob = 100.0