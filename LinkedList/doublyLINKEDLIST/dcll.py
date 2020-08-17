class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        ptr1 = Node(data)
        temp =self.head

        ptr1.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            ptr1.prev = temp
            temp.next = ptr1
            temp.prev = ptr1
        else:
            ptr1.next = ptr1
            ptr1.prev = ptr1
        self.head = ptr1
    
    def search(self, value):
        temp = self.head
        while temp.next != self.head:
            if temp.data ==  value:
                print("found")
            temp = temp.next
            
            
    
    def display(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break



llist = DoublyLinkedList()
llist.push(3)
llist.push(2)
llist.push(1)
llist.push(20)
llist.push(56)
llist.display()
val = int(input("Enter the item you want to search\n"))
llist.search(val)