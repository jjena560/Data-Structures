def swap(a,b):
    temp = arr[i]
    arr[i]= arr[0]
    arr[0] = temp
    return arr[0], arr[i]


arr = [5, 4, 6, 3, 9, 78]
n= int(input("Enter the number you want to search\n"))
for i in range(len(arr)):
    if arr[i] == n:
        print('found')
        swap(i, 0)
        print(arr)
        quit()
for i in range((len(arr))):
    if arr[i]!=n:
        query = input('Not Found\nDo you want to add the number to the list?\nY/N?')
        Fl = query[0].lower()
        if query == '' or Fl not in ['y', 'n']:
            print('Please answer with yes or no!')

        elif Fl == 'y':
            arr.append(n)
            print("number added\n")
            print(arr)
            quit()
            break
        elif Fl == 'n':
            quit()
            break


