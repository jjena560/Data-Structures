class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.row = None
        self.col = None


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
        print("row position:", end =" ")
        while temp:
            print(temp.row, end=" ")
            temp = temp.next
        print("\n")
        print("col position", end=" ")
        temp = self.head
        while temp:
            print(temp.col, end=" ")
            temp = temp.next
        print("\n")
        print("non-zero value", end=" ")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def createNode(self, mat, i, j):
        temp = self.head
        if temp is None:
            new_node = Node(mat)
            new_node.row = i
            new_node.col = j
            self.head = new_node
        else:
            while temp.next is not None:
                temp = temp.next
            r = Node(mat)
            r.row = i
            r.col = j
            r.next = None
            temp.next = r


matrix = [[0, 0, 3, 0, 4], [0, 0, 5, 7, 0], [0, 0, 0, 0, 0], [0, 2, 6, 0, 0]]
ll = LinkedList()

for i in range(4):
    for j in range(5):
        if matrix[i][j] != 0:
            ll.createNode(matrix[i][j], i, j)
ll.printList()
