def duplicate_bit(string):
    string = string.lower().replace(" ","")
    h = 0
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    x =  0
    for i in range(len(string)):
        c = ord(string[i])
        x = 1
        if string[i] in num:
            x = x<<c
            if x & h > 0:
                print("duplicate found  ",string[i])
            else:
                h = h|x
        else:
            x = x << c-97
            if x & h > 0:
                print("duplicate found  ",string[i])
            else:
                h = h|x

str = 'Jyotiprakash Jena'
duplicate_bit(str)
