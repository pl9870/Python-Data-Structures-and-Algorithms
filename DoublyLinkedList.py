#  Feel free to use this implementation of Doubly Linked Lists in your own code and change or add whatever you would like
# (Sorry for being lazy and not raising exceptions....)
#  As of now there only four methods :(
#  Author: pl9870

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def set_next(self, data):
        self.next = data
        data.prev = self
    
    def set_prev(self, data):
        self.prev = data
        data.next = self
    
    def set_data(self, data):
        self.data = data

class DoublyLinkedList:
    def __init__(self, root):
        self.head = root
        self.tail = root
        self.size = 1

    def size(self):
        return self.size

    def append(self, data):  #appends a node at the end of the list
        self.tail.set_next(data)
        self.tail = data
        self.size += 1

    def cut(self):  #cuts the last node off the list
        if self.size == 1:
            return "Error: Cutting would get rid of all elements"
        temp = self.tail
        self.tail = self.tail.prev
        temp.prev = None
        self.tail.next = None
        self.size -= 1

    def insert(self, n, data): #inserts node into the nth node with the head counted as 1
        if n > self.size + 1:
            return "Error: IndexOutOfBounds"
        elif n == self.size + 1:
            self.append(data)
        else:
            temp = self.head
            for i in range(1,n):
                temp = temp.next
            data.set_prev(temp.prev)
            data.set_next(temp)
            if n == 1:
                self.head = data
            self.size += 1

    def remove(self, data): #removes data
        if self.size == 1:
           return "Error: Cutting would get rid of all elements"
        temp = self.head
        while temp != data:
            temp = temp.next  #this is the data point we want to remove
        if temp == self.head:
            temp2 = self.head
            self.head = self.head.next
            temp2.next = None
            self.head.prev = None
            self.size -= 1
        elif temp == self.tail:
            self.cut()
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.next = None
            temp.prev = None
            self.size -= 1


#Smoke Testing
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
L = DoublyLinkedList(n1)
L.append(n2)
L.append(n3)
print(L.head.data)
print(L.tail.data)
print(n1.next.data)
print(n2.prev.data)
L.cut()
print(L.tail.data)
L.remove(n2)
print(L.head.data)
print(L.tail.data)
print(L.remove(n1))
print(L.cut())
L.append(n2)
L.insert(2,n3)
print(n1.next.data)
print(n1.next.next.data)

#Expected Testing
#1
#3
#2
#1
#2
#1
#1
#Error: Cutting would get rid of all elements
#Error: Cutting would get rid of all elements
#3
#2
