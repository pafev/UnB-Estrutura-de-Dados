class Node():
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    def setData(self, newdata):
        self.data = newdata
    def getData(self):
        return self.data
    def setNext(self, newnext):
        self.next = newnext
    def getNext(self):
        return self.next

class UnorderedList():
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    def search(self, item):
        current = self.head
        found = False
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self, item):
        previous = None
        current = self.head
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    def index(self, item):
        current = self.head
        count = 0
        while current.getData() != item:
            count += 1
            current = current.getNext()
        return count
    def insert(self, pos, item):
        temp = Node(item)
        if pos == 0:
            temp.setNext(self.head)
            self.head = temp
        else:
            current = self.head
            count = 0
            while count < pos - 1:
                current = current.getNext()
                count += 1
            temp.setNext(current.getNext())
            current.setNext(temp)
