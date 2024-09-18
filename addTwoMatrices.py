def addition(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        print("Error! Matrices must have same dimensions.")

    result = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]

    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j] = mat1[i][j] + mat2[i][j]

    return result

matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

result = addition(matrix1,matrix2)

for row in result:
    print(result)