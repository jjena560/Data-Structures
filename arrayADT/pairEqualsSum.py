def pairOfElements(arr, value):
    for i in range(len(arr)):
        k = i+1
        for j in range(k, len(arr)):
            if arr[i] + arr[j] == value:
                print("sum of values at index- "+str(i),str(j)+" is equals to "+ str(value))


    return arr

arr = [6, 3, 8, 10, -16, -13, 5, 2, 9, 14]
pairOfElements(arr, 10)
