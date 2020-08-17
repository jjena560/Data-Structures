def printMatrix(mat, r, c):
    for i in range(r):
        for j in range(c):
            print(mat[i][j], end=" ")
        print()

def lowerTraingular(mat, r, c):
    for i in range(r):
        for j in range(c):
            if i!=j and not i > j:
                mat[i][j] = 0

    printMatrix(mat, r, c)

def upperTraingular(mat, r, c):
    for i in range(r):
        for j in range(c):
            if i!=j and not i < j:
                mat[i][j] = 0
    printMatrix(mat, r, c)


if __name__ == "__main__":
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))

    # Initialize matrix
    matrix = []
    print("Enter the entries rowwise:")

    # For user input
    for i in range(R):  # A for loop for row entries
        a = []
        for j in range(C):  # A for loop for column entries
            a.append(int(input()))
        matrix.append(a)

    # lowerTraingular(matrix, R, C)
    print('\n')
    upperTraingular(matrix, R, C)