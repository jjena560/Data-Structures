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

    # def reverse(self):
    #     prev = None
    #     current = self.head
    #     while current is not None:
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next
    #     self.head = prev

    # def reverse(self):
    #     a = [0]*5
    #     i =0
    #     temp = self.head
    #     while temp is not None:
    #         a[i] = temp.data
    #         i += 1
    #         temp = temp.next
    #
    #     temp = self.head
    #     i -= 1
    #     while temp is not None:
    #         temp.data = a[i]
    #         temp = temp.next
    #         i -= 1


ll =LinkedList()
ll.push(3)
ll.push(5)
ll.push(6)
ll.push(8)
ll.push(7)
ll.reverse()
ll.printList()