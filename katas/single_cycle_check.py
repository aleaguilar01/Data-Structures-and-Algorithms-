def has_single_cycle(array):
    visited = {}
    index_in_array = 0
    counter = 0

    while counter < len(array):
        if len(array) > index_in_array >= 0:
            index_in_array = index_in_array + array[index_in_array]

        if index_in_array > len(array) - 1:
            index_in_array = index_in_array - len(array)
        elif index_in_array < 0:
            index_in_array = len(array) + index_in_array


        if len(array) > index_in_array >= 0:
            if index_in_array not in visited:
                visited[index_in_array] = True
                counter += 1
            else:
                return False

    return True

arr = [2, 3, 1, -4, -4, 2]

print(has_single_cycle(arr))
