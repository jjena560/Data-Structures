class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def append(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        if self.head is None:
            self.head = new_node
            return
        while (temp.next):
            temp = temp.next
        temp.next = new_node

    def deleteList(self):
        temp = self.head
        while(temp):
            prev = temp.next
            del temp
            temp = prev



    def getNth(self, index):
        current = self.head  # Initialise temp
        count = 0  # Index of current node

        # Loop while end of linked list is not reached
        while (current):
            if (count == index):
                return current.data
            count += 1
            current = current.next

        # if we get to this line, the caller was asking
        # for a non-existent element so we assert fail
        assert (False)
        return 0;
ll = LinkedList()

for i in range(9):
    ll.append(i)

ll.printList()

print(ll.getNth(3))