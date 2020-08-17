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

    #using hash table
    def detectLoop(self):
        p = self.head
        q = self.head
        while p and q and q.next:
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.head.next.next.next.next = llist.head

if (llist.detectLoop()):
    print("Loop found")
else:
    print("No Loop ")

