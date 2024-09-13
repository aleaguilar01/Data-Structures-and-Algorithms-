def formingMagicSquare(s):
    repeated_numbers = []
    missing_numbers = []


    numbers = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }

    index_1 = 0

    while index_1 < len(s):
        index_2 = 0
        while index_2 < len(s[0]):
            current_number = s[index_1][index_2]
            if numbers[current_number] == 1:
                repeated_numbers.append(current_number)
            else:
                numbers[current_number] += 1
            index_2 += 1
        index_1 += 1

    for number in numbers:
        if numbers[number] == 0:
            missing_numbers.append(number)

    for number in repeated_numbers:
        missing_numbers_index = 0
        if number == s[0][1]:
            s[0][1] = missing_numbers[missing_numbers_index]
        elif number == s[1][0]:
            s[1][0] = missing_numbers[missing_numbers_index]
        elif number == s[1][2]:
            s[1][2] = missing_numbers[missing_numbers_index]
        elif number == s[2][1]:
            s[2][1] = missing_numbers[missing_numbers_index]
        elif number == s[0][0]:
            s[0][0] = missing_numbers[missing_numbers_index]
        elif number == s[0][2]:
            s[0][2] = missing_numbers[missing_numbers_index]
        elif number == s[2][0]:
            s[2][0] = missing_numbers[missing_numbers_index]
        elif number == s[2][2]:
            s[2][2] = missing_numbers[missing_numbers_index]

        missing_numbers_index += 1

    return s


s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]





print(formingMagicSquare(s))

