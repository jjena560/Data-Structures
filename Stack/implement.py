class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, stack, item):
        self.stack.append(item)
        print("item pushed into stack", item)

    def pop(self, stack):
        if len(self.stack) == 0:
            print("empty stack")
            return
        return self.stack.pop()

    def peek(self, stack):
        return self.stack[len(self.stack)-1]

stack = Stack()
stack.push(stack, 3)
stack.push(stack, 5)
stack.push(stack, 9)
stack.push(stack, 21)

print(stack.pop(stack))
print(stack.peek(stack))
