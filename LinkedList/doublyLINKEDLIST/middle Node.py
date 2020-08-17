import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def middle(self):
        temp = self.head
        q = self.head
        i = 0
        while temp:
            temp = temp.next
            i += 1
        for j in range(math.floor(i/2)):
            q = q.next
        return q.data

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


llist =LinkedList()
for i in range(7):
    llist.append(i)

print(llist.middle())