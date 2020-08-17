arr = [4, 8, 30, 15, 28, 21, 24, 27]


def insertionSort(arr, x):
    arr.append(x)
    for i in range(1, len(arr)):
        currentVal = arr[i]
        pos = i
        while currentVal < arr[pos-1] and pos>0:
            arr[pos] = arr[pos-1]
            pos -= 1
        arr[pos] = currentVal

    return arr

print(insertionSort(arr, 13))