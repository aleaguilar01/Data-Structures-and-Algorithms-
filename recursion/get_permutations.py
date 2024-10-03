def get_permutations(array):

    def swap(arr, i, j):
        arr[i], arr[j] = arr[j] , arr[i]

    def helper(i, arr, permutations):
        if i == len(arr) - 1:
            permutations.append(arr[:])

        else:
            for j in range(i, len(arr)):
                swap(arr, i, j)
                helper(i + 1, arr, permutations)
                swap(arr, i, j)

    permutations = []

    helper(0, array, permutations)

    return permutations

list = [1, 2, 3]

print(get_permutations(list))
