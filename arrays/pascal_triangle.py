def get_pascal_triangle(n):
    pascal_triangle = []

    for i in range(n):
        new_row = [1]
        index1 = 0
        index2 = 1
        while index1 < n and index2 < n:
            for j in range(i):
                if j % 2 == 0:


        new_row.append(1)
