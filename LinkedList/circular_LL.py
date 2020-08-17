class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        ptr1 = Node(new_data)
        temp = self.head

        ptr1.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = ptr1
        else:
            ptr1.next = ptr1
        self.head = ptr1



    def display(self):
        temp =  self.head
        if self.head is not None:
            while True:
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break






llist = CircularLinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.display()