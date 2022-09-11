#Fazendo como uma lista de listas
myTree = ['root', ['leftSubtree',[],[]], ['rightSubtree',[],[]]]

def binaryTree(root):
    return [root, [], []]

def insertLeft(root, childValue):
    temp = root.pop(1)
    if temp:
        root.insert(1, [childValue, temp, []])
    else:
        root.insert(1, [childValue, [], []])

def insertRight(root, childValue):
    temp = root.pop()
    if temp:
        root.append([childValue, [], temp])
    else:
        root.append([childValue, [], []])

def getRootValue(root):
    return root[0]

def setRootValue(root, newValue):
    root[0] = newValue

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def getLeftChildValue(root):
    return root[1][0]

def getRightChildValue(root):
    return root[2][0]

