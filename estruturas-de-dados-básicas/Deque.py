class Deque():
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    def addFront(self, item):
        self.items.insert(0, item)
    def removeFront(self):
        if self.items:
            return self.items.pop(0)
    def addRear(self, item):
        self.items.append(item)
    def removeRear(self):
        if self.items:
            return self.items.pop()