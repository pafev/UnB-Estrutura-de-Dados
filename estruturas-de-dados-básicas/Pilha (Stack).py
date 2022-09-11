class Stack():
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.items:
            return self.items.pop()
    def peek(self):
        if self.items:
            return self.items[len(self.items) - 1]
    def isEmpty(self):
        return self.items == []