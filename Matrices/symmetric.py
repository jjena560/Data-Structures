def transpose(mat, tr, r, c):

    for i in range(r):
        for j in range(c):
            tr[i][j] = mat[j][i]

def isSymmetric(mat, r, c):
    tr = [ [0 for j in range(c) ] for i in range(r) ]
    transpose(mat, tr, r, c)
    for i in range(r):
        for j in range(c):
            if (mat[i][j] != tr[i][j]):
                return False
            return True



mat = [ [ 1, 3, 5 ], [ 3, 2, 4 ], [ 5, 4, 1 ] ]
if (isSymmetric(mat, 3, 3)):
    print("Yes")
else:
    print("No")