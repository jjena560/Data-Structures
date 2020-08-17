matrix = [[0, 0, 7, 2, 0], [2, 9, 0, 5, 0], [9, 0, 0, 4, 0], [0, 0, 0, 0, 4]]
size = 0
for i in range(4):
    for j in range(5):
        if matrix[i][j] != 0:
            size += 1

rows, cols = (3, size)
compactMatrix = [[0 for i in range(cols)] for j in range(rows)]
k = 0
for i in range(4):
    for j in range(5):
        if matrix[i][j] != 0:
            compactMatrix[0][k] = i
            compactMatrix[1][k] = j
            compactMatrix[2][k] = matrix[i][j]
            k += 1

print(compactMatrix)
