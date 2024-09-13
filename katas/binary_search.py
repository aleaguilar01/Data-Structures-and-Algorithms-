def binary_search(array, item):
    initial_index = 0
    end_index = len(array) - 1

    while initial_index <= end_index:
        mid_index = initial_index + round(end_index - initial_index)
        mid_value = array[mid_index]
        if mid_value == item:
            return mid_index
        elif item < mid_value:
            end_index = mid_index - 1
        else:
            initial_index = mid_index + 1

    return -1

print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73],0))