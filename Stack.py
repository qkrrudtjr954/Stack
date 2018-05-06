class Stack :
    class Item :
        def __init__(self, data) :
            self.data = data
            self.next = None

    def __init__(self) :
        self.size = 0
        self.top = None

    def push(self, data) :
        newItem = self.Item(data)
        # if it is not empty stack,
        # then store this item to top
        if self.top != None :
            newItem.next = self.top

        # newItem becomes top
        self.top = newItem
        self.size += 1

    def pop(self) :
        # if stack is empty,
        # then return None
        result = self.top
        if result != None :
            self.top = result.next
            self.size -= 1
            return result.data
        else :
            return None

    def peek(self) :
        if self.top != None :
            return self.top.data
        else :
            return None

    def isEmpty(self) :
        if self.top == None and self.size == 0:
            return True
        else :
            return False

    def getSize(self) :
        return self.size

    def show(self) :
        result = []
        curr = self.top

        while curr != None :
            result.append(curr.data)
            curr = curr.next

        return result
