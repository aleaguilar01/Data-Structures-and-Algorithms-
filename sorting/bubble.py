from swap import *


def bubble_sort_a(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
    return arr


def bubble_sort_b(arr):
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range (0, len(arr)-1):
            if arr[i] > arr[i + 1]:
                swap(arr, arr[i], arr[i+1])
                is_sorted = False

    return arr


new_list = [23, 4, 56, 7, 89, 10, 3, 67]

print(bubble_sort_a(new_list))
print(bubble_sort_b(new_list))
