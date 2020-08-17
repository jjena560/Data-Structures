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
        self.head = new_node

    def reverse(self):
        temp = None
        current = self.head
        while current:

            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = current.prev
        if current is None:
            return current


    def display(self):
        temp = self.head
        if self.head is not None:
            while temp is not None:
                print(temp.data)
                temp = temp.next


llist = DoublyLinkedList()
llist.push(1)
llist.push(2)
llist.push(3)


llist.reverse()
llist.display()