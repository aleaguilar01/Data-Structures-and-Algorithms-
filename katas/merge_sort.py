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

    results.extend(arr1[index1:])
    results.extend(arr2[index2:])

    return results


def mergeSort(array):
    if len(array) <= 1:
        return array

    mid = round(len(array) / 2)
    left_array = mergeSort(array[:mid])
    right_array = mergeSort(array[mid:])

    return merge(left_array, right_array)


print(mergeSort([1,2,8,7,-12,14,120,0,-5,35]))