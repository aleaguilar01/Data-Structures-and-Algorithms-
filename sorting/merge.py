def merge(arr1, arr2):
    results = []
    index1 = 0
    index2 = 0

    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] <= arr2[index2]:
            results.append(arr1[index1])
            index1 += 1
        else:
            results.append(arr2[index2])
            index2 += 1

    results.extend(arr1[index1:] + arr2[index2:])
    return results


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle_of_array = round(len(arr)/2)
    left_array = merge_sort(arr[:middle_of_array])
    right_array = merge_sort(arr[middle_of_array:])
    return merge(left_array, right_array)


list_a = [16, 19, 4, 32, 4, 1, 90, 100, 0]


print(merge_sort(list_a))






