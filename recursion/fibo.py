Fib = []
def fib(n):
    if n<=1:
        Fib[n] = n
        return n
    if Fib[n] == None:
        Fib[n-2]= fib(n-2)
        Fib[n-1] = fib(n-1)
        return Fib(n-2)+Fib(n-1)


print(fib(6))