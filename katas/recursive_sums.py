def productSum(values, depth=1):
    sum = 0

    for x in values:
        if isinstance(x, list):
            sum += productSum(x, depth + 1)
        else:
            sum += (x * depth)
    return sum



arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

print(productSum(arr))