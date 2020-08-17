class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAt(self, data, pos):
        temp = self.head
        new_node = Node(data)
        if self.head is not None:
            for i in range(pos-1):
               temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        
        else:
            self.head = new_node

    def insertBeforeHead(self, data):
        temp = self.head
        new_node = Node(data)

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

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

llist.insertAt(5, 2)

# (llist.insertBeforeHead(6))
llist.display()