def transpose(mat1):
    rows = len(mat1)
    cols = len(mat1[0])

    mat2 = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            mat2[j][i] = mat1[i][j]

    return mat2

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = transpose(matrix1)

for row in result:
    print(row)
