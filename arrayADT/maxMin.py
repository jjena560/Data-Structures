max = 0
def maxMin(arr):
    min = arr[0]
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i]>max:
            max = arr[i]

    return min, max


arr = [6, 3, 8, 10, -16, -13, 5, 2, 9, 14]
print(maxMin(arr))