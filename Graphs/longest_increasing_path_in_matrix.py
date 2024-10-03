def longest_increasing_path_in_matrix(matrix):
    longest_route = 0
    visited = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(False)
        visited.append(row)

    def visit_neighbor(i,j, length_path = 0):
        length_path += 1
        visited[i][j] = True
        down = 0
        right = 0

        if i < len(matrix) -1 and j < len(matrix[i]) - 1 and matrix[i][j+1] <= matrix[i][j] and matrix[i+1][j] <= matrix[i][j]:
            return length_path

        if i < len(matrix) - 1 and matrix[i+1][j] > matrix[i][j] and not visited[i+1][j]:
            down = visit_neighbor(i+1, j, length_path)
        if j < len(matrix[i]) - 1 and matrix[i][j+1] > matrix[i][j] and not visited[i][j+1]:
            right = visit_neighbor(i, j+1, length_path)

        return max(length_path,max(down, right))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not visited[i][j]:
                current_route = visit_neighbor(i, j)
                longest_route = max(longest_route, current_route)

    return longest_route




m = [
    [1,2],
    [3,4]
]
print(longest_increasing_path_in_matrix(m))



# l = [
#     [1,2,3,3],
#     [2,2,4,5],
#     [3,6,7,6],
#     [3,5,8,9]
# ]
#
# print(longest_increasing_path_in_matrix(l))
#
#
# r = [
#     [1,2,3,3],
#     [2,1,4,5],
#     [2,2,7,6],
#     [2,3,4,5]
# ]
#
# print(longest_increasing_path_in_matrix(r))
