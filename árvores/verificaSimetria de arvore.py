class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

leftPreOrderList = []
rightPreOrderList = []

def leftPreOrder(raiz):
    if raiz:
        leftPreOrderList.append(raiz.dado)
        leftPreOrder(raiz.esq)
        leftPreOrder(raiz.dir)

def rightPreOrder(raiz):
    if raiz:
        rightPreOrderList.append(raiz.dado)
        rightPreOrder(raiz.dir)
        rightPreOrder(raiz.esq)

def verificaSimetria(raiz):
    global leftPreOrderList
    global rightPreOrderList
    leftPreOrder(raiz.esq)
    rightPreOrder(raiz.dir)
    if leftPreOrderList == rightPreOrderList:
        leftPreOrderList = []
        rightPreOrderList = []
        return True
    else:
        leftPreOrderList = []
        rightPreOrderList = []
        return False