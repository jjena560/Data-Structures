def createStack():
    stack = []
    return stack

def push(stack, item):
    stack.append(item)

def pop(stack):
    return stack.pop()

def reverse(string):
    n = len(string)
    try:
        stack = createStack()
        for i in range(n):
            push(stack, string[i])
        string = ""
        for i in range(n):
            string += pop(stack)
        print(string)
    except IOError:
        print("invalid input")

string = input("enter the string you want to reverse: ")
print("string before getting reversed: ", end="")
print(string)
print("string after getting reversed: ", end="")
print(reverse(string))
