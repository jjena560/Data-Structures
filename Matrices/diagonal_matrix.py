def printmatrix(mat, n, m):
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")

        print()

    # Function to change the values

def makenondiagonalzero(mat, n, m):
    # Traverse all non-diagonal elements
    for i in range(n):
        for j in range(m):
            if i != j and i + j + 1 != n:
                # Change all non-diagonal
                # elements to zero  
                mat[i][j] = 0

    # print resultant matrix  
    printmatrix(mat, n, m)

if __name__ == "__main__":
    # A basic code for matrix input from user

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

    #     # For printing the matrix
    # for i in range(R):
    #     for j in range(C):
    #         print(matrix[i][j], end=" ")
    #     print()
    print(a)
    print(matrix)

    makenondiagonalzero(matrix, R, C)