def duplicates(a, n):
    Max = max(a)
    Hash = [0] * (Max+1)

    for i in  range(n):
        Hash[a[i]] += 1
    for h in range(len(Hash)):
        if Hash[h]!=0:
            print(str(h)+ ' is in the list '+str(Hash[h])+' time(s)')

    return Hash


a = [6, 7, 8, 9, 11, 6, 8]
n = len(a)

print(duplicates(a, n))