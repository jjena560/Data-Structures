strn = '35*4+'
arr = []

for i in strn:
    if i.isdigit():
        arr.append(i)
    else:
        x = arr.pop()
        y = arr.pop()
        arr.append(str(eval(x + i + y)))

print(arr)
x = '5'
y = '6'
z = '*'
print(eval(x + z + y))