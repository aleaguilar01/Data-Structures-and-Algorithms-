def twoNumberSum(array, targetSum):
    sums_dictionary = {}

    for number in array:
        missing_number = targetSum - number

        if missing_number in sums_dictionary:
            return [number, missing_number]

        sums_dictionary[number] = missing_number

    return []

    pass
