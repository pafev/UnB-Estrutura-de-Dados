tamanhoCaminhos = []
temp = 0

class BinaryTree():
    def __init__(self, data):
        self.dado = data
        self.esq = None
        self.dir = None

def mostraAltura(raiz):
    global tamanhoCaminhos
    global temp
    if raiz.dado:
        if raiz.dir:
            temp += 1
            mostraAltura(raiz.dir)
            temp -= 1
        if raiz.esq:
            temp += 1
            mostraAltura(raiz.esq)
            temp -= 1
        temp2 = temp
        tamanhoCaminhos.append(temp2)
        del temp2

def addChild(raiz, value):
    subTree = BinaryTree(value)
    if value < raiz.dado:
        if raiz.esq == None:
            raiz.esq = subTree
        else:
            del subTree
            addChild(raiz.esq, value)
    elif value > raiz.dado:
        if raiz.dir == None:
            raiz.dir = subTree
        else:
            del subTree
            addChild(raiz.dir, value)

n = int(input())
values = list(map(int, input().split()))

raiz = BinaryTree(values[0])
for i in values[1:]:
    addChild(raiz, i)

mostraAltura(raiz)

print(max(tamanhoCaminhos))