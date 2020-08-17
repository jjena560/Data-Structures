# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
    # next as null


# Linked List class
class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head #now temp stores the address of the first node i.e. llist.head
        while(temp):
            print(temp.data) #first temp will get the value of llist.head.data
            temp = temp.next #then temp wll store the address of second node

# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2) #second node object
    third = Node(3) #third node object

    llist.head.next = second  # Link first node with second

    second.next = third

    print(llist.head.data)

