def rev(string):
    n = len(string)
    j = n-1
    b = [0] * (n)
    for i in range(n):
        b[j]= string[i]
        j -= 1
    return b

print(rev('hello'))
