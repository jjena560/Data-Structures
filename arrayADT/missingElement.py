arr = [6, 7, 8, 9, 11, 14, 16, 17]
low = arr[0]
diff = low - 0

for i in range(len(arr)):
    if arr[i]-i != diff:
        while diff < arr[i] - i:
            print("missing element-"+ str(i+diff))
            diff += 1