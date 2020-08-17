class Paranthesis:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.arr = []
        self.output = []
        self.open = ['(', '{', '[']
        self.close =  [')', '}', ']']

    def push(self, char):
        self.top += 1
        self.arr.append(char)

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isPara(self, ch):
        
        if ch in self.open:
            return True
        else:
            return False
    def isClose(self, ch):
        
        if ch in self.close:
            return True
        else:
            return False

    def peek(self):
        return self.arr[-1]


    def pop(self):
        self.top -= 1
        return self.arr.pop()

    def isOperand(self, ch):
        return ch.isalpha()

    def balance(self, exp):
        for i in exp:
            if self.isPara(i):
                self.push(i)
            elif self.isClose(i):
                pos = self.close.index(i)
                if not self.isEmpty() and self.peek() == self.open[pos]:
                    self.pop()
            else:
                continue
        print(self.arr)
        if self.isEmpty():
            print("balanced")
        else:
            print("not balanced")




exp = "([]}"
obj = Paranthesis(len(exp))
obj.balance(exp)
