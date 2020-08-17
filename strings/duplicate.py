def duplicate(string):
    n = len(string)
    for i in range(n):
        k =i+1
        for j in range(k, n):
            if string[i] == string[j]:
                print("found", string[i])


duplicate('jpj')