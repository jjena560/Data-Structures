class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
        self.head = new_node

    def insertAt(self, data, pos):
        temp = self.head
        new_node = Node(data)
        if self.head is not None:
            if pos == 0:
                new_node.next = self.head
                new_node.prev = None
                self.head = new_node
            else:
                for i in range(pos-1):
                    temp = temp.next
                new_node.next = temp.next
                new_node.prev = temp
                if temp.next is not None:
                    temp.next = new_node
                    temp.next.prev = new_node
                temp.next = new_node

    def display(self):
        temp = self.head
        if self.head is not None:
            while temp is not None:
                print(temp.data)
                temp = temp.next


llist = DoublyLinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.push(16)
llist.insertAt(18,0)
llist.insertAt(25, 2)
llist.display()