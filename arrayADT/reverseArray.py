arr = [4, 8, 24, 10, 12, 18, 19]


def revArray(arr):
    last = len(arr) - 1
    first = 0
    # while first < last:
    #     arr[first], arr[last] = arr[last], arr[first]
    #     revArray(arr, first+1, last-1)
    #     return arr
    while first < last:
        arr[first], arr[last] = arr[last], arr[first]
        first += 1
        last -= 1
    return arr

print(revArray(arr))

