def transposeMatrix(matrix):
    transposed = []

    inside_index = 0

    while inside_index < len(matrix[0]):
        list = []
        for outside_index in range(len(matrix)):
            list.append(matrix[outside_index][inside_index])
        transposed.append(list)
        inside_index += 1

    return transposed

matrix = [[1,2], [3,4], [5,6]]



print(transposeMatrix(matrix))