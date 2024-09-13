def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    index_1 = 0
    index_2 = 0
    smallest = float("inf")
    smallest_pair = []

    while index_1 < len(arrayOne) and index_2 < len(arrayTwo):
        number_1 = arrayOne[index_1]
        number_2 = arrayTwo[index_2]

        current = abs(number_1 - number_2)

        if current < smallest:
            smallest = current
            smallest_pair = [number_1, number_2]

        if number_1 < number_2:
           index_1 += 1
        elif number_1 > number_2:
            index_2 += 1
        else:
            return [number_1, number_2]

    return smallest_pair

print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))