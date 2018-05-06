from LinkedList import LinkedList

class Stack :
    def __init__(self) :
        self.store = LinkedList()
        self.size = 0

    def push(self, data) :
        self.size += 1
        self.store.addFirst(data)

    def pop(self) :
        result = self.store.get(0)
        self.size -= 1
        self.store.removeFirst()
        return result

    def peek(self) :
        result = self.store.get(0)
        return result

    def isEmpty(self) :
        if self.size == 0:
            return True
        else :
            return False

    def getSize(self) :
        return self.size

    def show(self) :
        return self.store.show()
