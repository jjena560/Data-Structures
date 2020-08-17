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

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        rest = self.reverse(head.next)
        q = head.next
        q.next = head
        head.next = None

        return rest

ll = LinkedList()
ll.push(20)
ll.push(4)
ll.push(18)
ll.push(45)

ll.head = ll.reverse(ll.head)
ll.printList()