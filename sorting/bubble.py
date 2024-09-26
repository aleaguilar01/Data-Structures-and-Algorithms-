def swap(arr, index_1, index_2):
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]


def bubble_sort(arr):
    for i in range(len(arr), 0, -1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
    return arr


def bubble_sort_optimized(arr):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap(arr, i, i+1)
                sorted = False

    return arr


new_list = [23, 4, 56, 7, 89, 10, 3, 67]

print(bubble_sort(new_list))
print(bubble_sort_optimized(new_list))
