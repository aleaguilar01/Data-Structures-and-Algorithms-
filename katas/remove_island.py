def transverse_matrix(matrix, visited, i, j, island_indexes=[]):
    current = matrix[i][j]

    visited[i][j] = True
    is_island = True

    if current == 0 or i == 0 or i == len(matrix) - 1 or j == 0 or j == len(matrix[0]) - 1:
        return False

    if matrix[i - 1][j] and not visited[i - 1][j]:
        is_neighbor_island = transverse_matrix(matrix, visited, i - 1, j, island_indexes)
        if not is_neighbor_island and matrix[i - 1][j] == 1:
            is_island = False
    if matrix[i + 1][j] and not visited[i + 1][j]:
        is_neighbor_island = transverse_matrix(matrix, visited, i + 1, j, island_indexes)
        if not is_neighbor_island and matrix[i + 1][j] == 1:
            is_island = False
    if matrix[i][j - 1] and not visited:
        is_neighbor_island = transverse_matrix(matrix, visited, i, j - 1, island_indexes)
        if not is_neighbor_island and matrix[i][j - 1] == 1:
            is_island = False
    if matrix[i][j + 1] and not visited:
        is_neighbor_island = transverse_matrix(matrix, visited, i, j + 1, island_indexes)
        if not is_neighbor_island and matrix[i][j + 1] == 1:
            is_island = False

    if is_island:
        island_indexes.append([i, j])

    return island_indexes


def removeIslands(matrix):
    visited = []
    island_indexes = []

    for row in matrix:
        visited_row = []
        for column in matrix[0]:
            visited_row.append(False)
        visited.append(visited_row)

    for row in range(1, len(matrix) - 1):
        for column in range(1, len(matrix[0]) - 1):
            if not visited[row][column] and matrix[row][column] == 1:
                island_indexes = transverse_matrix(matrix, visited, row, column)

    return island_indexes



matrix = [
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1]
]

result = removeIslands(matrix)

print(result)