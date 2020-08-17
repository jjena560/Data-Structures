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

    def sumofNodes(self):
        temp = self.head
        sum = 0
        while temp is not None:
            sum += temp.data
            temp = temp.next
        return sum


ll = LinkedList()
for i in range(4):
    ll.push(i)

print(ll.sumofNodes())




