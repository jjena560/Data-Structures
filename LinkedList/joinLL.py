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


    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def merge(self, head1, head2):
        temp = None
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        if head1.data <= head2.data:
            temp = head1
            temp.next = self.merge(head1.next, head2)
        else:
            temp = head2
            temp.next = self.merge(head1, head2.next)

        return temp

ll1 = LinkedList()
ll2 = LinkedList()
ll1.append(2)
ll1.append(8)
ll1.append(10)
ll1.append(15)
ll2.append(4)
ll2.append(7)
ll2.append(12)
ll2.append(14)

ll3 = LinkedList()
ll3.head = ll3.merge(ll1.head, ll2.head)

ll3.printList()
