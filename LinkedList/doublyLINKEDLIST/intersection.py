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

    def getIntersectionNode(self, head1, head2):

        curr1 = head1
        curr2 = head2

        while curr1.data != curr2.data:
            curr2 = curr2.next
            curr1 = curr1.next
        return curr1.data



    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


ll1 = LinkedList()
ll2 = LinkedList()
ll3 = LinkedList()
ll1.append(9)
ll1.append(15)
ll1.append(30)
ll2.append(10)
ll2.append(15)
ll2.append(30)

ll3.head = ll3.getIntersectionNode(ll1.head, ll2.head)

print(ll3.head)