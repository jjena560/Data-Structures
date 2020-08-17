class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head = new_node

    #to insert at a particular node
    def insertAfter(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        if self.head is None:
            self.head = new_node
            return  #if the list is empty
        while (temp.next):
            temp = temp.next
        temp.next = new_node
        
    
    def delNode(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if (temp == None):
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None


    def printList(self):
        temp = self.head #now temp stores the address of the first node i.e. llist.head
        while(temp):
            print(temp.data)
            temp = temp.next


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second
second.next = third

llist.push(5)
llist.insertAfter(second, 6)
llist.append(8)
llist.delNode(6)
llist.printList()