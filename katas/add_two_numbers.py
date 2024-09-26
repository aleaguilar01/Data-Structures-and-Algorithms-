def addTwoNumbers(l1, l2):
    results = []

    index = 0
    to_go = 0

    while index < len(l1) + 1 or index < len(l2) + 1:
        if index < len(l1):
            number_1 = l1[index]
        else:
            number_1 = 0

        if index < len(l2):
            number_2 = l2[index]
        else:
            number_2 = 0


        add = to_go + number_1 + number_2

        if add > 9:
            add = add - 10
            to_go = 1
        else:
            to_go = 0

        results.append(add)

        index += 1

    return results


l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

print(addTwoNumbers(l1, l2))