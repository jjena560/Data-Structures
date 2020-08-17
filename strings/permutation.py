def permutation(str, k):
    n = len(str)
    a = [0]*n
    res = [None]*n
    i = 0
    # for i in range(n):
    while i < n-1:
        if a[i] == 0:
            res[k] = str[i]
            a[i] = 1
            i += 1
            permutation(str, k+1)

    return res, i
string = 'ABC'
print(permutation(string, 0))
