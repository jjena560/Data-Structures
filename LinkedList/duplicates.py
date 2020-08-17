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

    #for sorted linked list

    def duplicateSorted(self):
        temp = self.head
        q = temp.next
        while q is not None:
            if temp.data == q.data:
                temp.next = q.next
                del q
                q = temp.next
            else:
                temp = q
                q = q.next

    #for unsorted
    def duplicateUnsorted(self):
        current = self.head
        q = None
        temp = None

        if self.head is None:
            return
        else:
            while current is not None:
                temp = current
                q = current.next
                while q is not None:
                    if current.data == q.data:
                        temp.next = q.next
                    else:
                        temp = q
                    q = q.next
                current = current.next


    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


ll = LinkedList()
ll.push(3)
ll.push(5)
ll.push(8)
ll.push(7)
ll.push(8)
ll.push(5)
ll.push(9)
ll.duplicateUnsorted()
ll.printList()