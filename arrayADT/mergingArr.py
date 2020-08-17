arr1 = [3, 8, 16, 20,22, 25]
arr2 = [4, 10, 12, 18,22, 23]
res = []


def merge(arr1, arr2):
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
            k += 1
        if arr1[i] == arr2[j]:
            res.append(arr1[i])
            i += 1
            j += 1
            k += 1
        else:
            res.append(arr2[j])
            j += 1
            k += 1
    if i <= len(arr1):
        res.append(arr1[i])
        i += 1
    elif j <= len(arr2):
        res.append(arr2[j])
        j += 1

    return res


print(merge(arr1, arr2))

