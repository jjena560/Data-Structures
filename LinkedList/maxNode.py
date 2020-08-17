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

    def max(self):
        temp = self.head
        max = -698236491261298619978778877878
        while(temp):
            if temp.data > max:
                max = temp.data
            temp = temp.next
        return max

    def min(self):
        temp = self.head
        min = 9803442152521350237092420957234
        while(temp):
            if temp.data < min:
                min = temp.data
            temp = temp.next
        return min

ll = LinkedList()
ll.append(4)
ll.append(12)
ll.append(45)
ll.append(3)

print(ll.max(),',', ll.min())


