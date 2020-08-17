def anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    n = len(str1)
    m = len(str2)
    if n == m:
        h = [0]*(26)
        for i in range(n):
            c = ord(str1[i])
            c = c-97
            h[c] +=1
        for j in range(m):
            c = ord(str2[j])
            c = c-97
            h[c] -= 1
            if h[c]<0:
                print("not anagram")
        if h == [0]*(26):
            print('anagram')

    else:
        print("lenth of the both the strings are not equal")
        exit()
    return h


str1 = 'jPjj'
str2 = 'pjjj'
print(anagram(str1, str2))