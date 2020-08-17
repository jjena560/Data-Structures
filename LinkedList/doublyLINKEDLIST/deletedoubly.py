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

    def delete(self, pos):
        temp = self.head
        if pos == 0:
            temp = temp.next
            self.head = temp
            self.head.next = temp.next
            self.head.prev = None
        else:
            for i in range(pos-1):
                temp = temp.next
            curr = temp.next
            temp.next = curr.next
            # curr.next.prev = temp

            del curr

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

llist.delete(2)
llist.display()