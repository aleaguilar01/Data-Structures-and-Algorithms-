def threeNumberSum(array, targetSum):
    results = []
    array.sort()

    for current_index in range(1, len(array) - 1):
        left_index = current_index - 1
        right_index = current_index + 1

        while left_index >= 0 and right_index < len(array):
            sum = array[left_index] + array[current_index] + array[right_index]
            if sum == targetSum:
                results.append((array[left_index], array[current_index], array[right_index]))
                left_index -= 1
                right_index += 1
            elif sum < targetSum:
                right_index += 1
            else:
                left_index -= 1

    print(sorted(results))


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
