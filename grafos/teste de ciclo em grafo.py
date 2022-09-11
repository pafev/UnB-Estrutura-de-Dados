class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.items:
            return self.items.pop()
    def isEmpty(self):
        return self.items == []

class Tree():
    def __init__(self, id):
        self.dado = id
        self.childs = []

def addNovosFilhos(tree, id, novosFilhos):
    if tree.dado == id and not tree.childs:
        for novoFilho in novosFilhos:
            temp = Tree(novoFilho)
            tree.childs.append(temp)
    else:
        for no in tree.childs:
            addNovosFilhos(no, id, novosFilhos)

def checaCiclo(tree):
    global temCiclo
    if tree.dado in caminho.items:
        temCiclo = True
    caminho.push(tree.dado)
    if not temCiclo:
        for filho in tree.childs:
            checaCiclo(filho)
            caminho.pop()

n = int(input())
id_raiz, A_raiz, *args = input().split()
tree = Tree(id_raiz)
if n < 4:
    for _ in args:
        temp = Tree(_)
        tree.childs.append(temp)

for i in range(n - 1):
    id, A, *novosFilhos = input().split()
    addNovosFilhos(tree, id, novosFilhos)

temCiclo = False
caminho = Stack()
checaCiclo(tree)

if temCiclo:
    print('Hoje tem!')
else:
    print('... que ama ninguem.')