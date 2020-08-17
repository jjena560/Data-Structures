class StackNode:
    def __init__(self, data):
        self.data  = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.root
        self.root = new_node
        print("Pushed to the stack ", data)


    def pop(self):
        if self.root is None:
            print("stack is empty")
            return
        temp = self.root
        self.root = self.root.next
        return temp.data

    def peek(self):
        if self.root is None:
            print("Empty stack")
            return
        return self.root.data

stack = Stack()
stack.push(3)
stack.push(6)
stack.push(21)
print(stack.peek())
