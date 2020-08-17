arr = [4, 8, 10, 15, 18, 21, 24, 27, 29, 33, 34, 37, 39, 41, 43, 100]




def getValAtIndex(arr, index):
    if index >=0 and index <= len(arr):
        return arr[index]
    else:
        print("index out of range")


def setValAtIndex(arr, index, value):
    if index >=0 and index <= len(arr)+1:
        arr[index] = value
        print('done')
        print(arr)
    else:
        print("invlid, enter the input correctly\n")
        
def maxValue(arr):
    max = 0
    if arr != '':
        for i in range(len(arr)):
            if arr[i]>max:
                max = arr[i]
    return max


