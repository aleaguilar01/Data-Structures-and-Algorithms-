def binary_search_recursive(key, array, min, max):
    if min > max:
        return -1

    midpoint = min + (max - min) // 2

    if array[midpoint] == key:
        return midpoint

    if array[midpoint] < key:
        return binary_search_recursive(key, array, midpoint+1, max)
    if array[midpoint] > key:
        return binary_search_recursive(key, array, min, midpoint-1)

list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#print(binary_search_recursive(20, list, 0, len(list)-1))

print(binary_search_recursive(5, list, 0, len(list)-1))
print(binary_search_recursive(15, list, 0, len(list)-1))
print(binary_search_recursive(6, list, 0, len(list)-1))