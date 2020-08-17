class Conversion:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.arr = []
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def push(self, char):
        self.top += 1
        self.arr.append(char)

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def isOperand(self, ch):
        return ch.isalpha() #inbuilt fucntion

    def peek(self):
        return self.arr[-1]

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            if a <= b:
                return True
            else:
                return False
        except KeyError:
            return False

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.arr.pop()
        else:
            return "$"

    def infixToPrefix(self, exp):
        for i in exp:
            # If the character is an operand,
            # add it to output
            if self.isOperand(i):
                self.output.append(i)
                    # An operator is encountered
            else:
                while (not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)

                # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())

        print("".join(self.output))

    def evaluatePostfix(self, exp):

        # Iterate over the expression for conversion
        for i in exp:

            # If the scanned character is an operand
            # (number here) push it to the stack
            if i.isdigit():
                self.push(i)

                # If the scanned character is an operator,
            # pop two elements from stack and apply it.
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))

        return int(self.pop())

            # Driver program to test above function

exp = "231*+9-"
obj = Conversion(len(exp))
print("postfix evaluation: %d" % obj.evaluatePostfix(exp))
