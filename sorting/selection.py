from swap import *

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)-1):
            if arr[min_index] > arr[j]:
                min_index = j
        if (i != min_index):
            swap(arr, i, min_index)
    return arr


a_list = [23,4,56,7,89,10,3,67]
b_list = [8, 1, 2, 3, 4, 5, 6, 7]
print(selection_sort(a_list))
print(selection_sort(b_list))