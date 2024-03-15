class ListBuf:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def add_value(self, val):
        if len(self.buffer) == self.capacity:
            self.buffer.pop(0)
        self.buffer.append(val)
    
    def print_buffer(self):
        print(self.buffer)

listA = ListBuf(3)
listA.add_value(1)
listA.add_value(2)
listA.add_value(3)
listA.add_value(4)
listA.add_value(1)

listA.print_buffer() #вывод 3 4 1

###

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class RefBuf:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head  #хвосту даем ссылку на первый элемент

    def remove(self):
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        return data

    def display(self):
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()


queue = RefBuf()
queue.add(1)
queue.add(2)
queue.add(3)
queue.display()
queue.remove()
queue.display() #вывод 2 3
queue.add(4)
queue.display() #вывод 2 3 4