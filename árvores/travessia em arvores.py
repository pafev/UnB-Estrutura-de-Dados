class binaryTree():
    def __init__(self, rootValue):
        self.key = rootValue
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self, childValue):
        if self.leftChild == None:
            self.leftChild = binaryTree(childValue)
        else:
            temp = binaryTree(childValue)
            temp.leftChild = self.leftChild
            self.leftChild = temp
    def insertRight(self, childValue):
        if self.rightChild == None:
            self.rightChild = binaryTree(childValue)
        else:
            temp = binaryTree(childValue)
            temp.rightChild = self.rightChild
            self.rightChild = temp
    def getRootValue(self):
        return self.key
    def setRootValue(self, newValue):
        self.key = newValue
    def getLeftChild(self):
        return self.leftChild
    def getRightChild(self):
        return self.rightChild

#agora vamos para as travessias
#preorder, postorder, inorder

def preorder(tree):
    if tree:
        print(tree.getRootValue())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootValue())

def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootValue())
        inorder(tree.getRightChild())