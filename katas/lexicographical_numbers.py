
def lexicalOrder(n):
    numbers_dic = {}
    result = []

    for num in range(1, n):
        if str(num)[0] not in numbers_dic:
            numbers_dic[str(num)[0]] = [num]
        else:
            numbers_dic[str(num)[0]].append(num)

    for key in numbers_dic:
        result.extend(numbers_dic[key])

    return result


#print(lexicalOrder(15))

def lexicalOrder_using_array(n):

    results = []

    if n > 9:
        num_array = [[] for _ in range(9)]
    else:
        num_array = [[] for _ in range(n)]

    for num in range(1,n+1):
        position = int(str(num)[0]) - 1
        num_array[position].append(num)

    for num in num_array:
        results.extend(num)

    return results

print(lexicalOrder_using_array(13))

def lexical_order_using_tree(n):
    results = []

    def dfs(current):
        if current > n:
            return
        results.append(current)
        for i in range(10):
            next_num = current * 10 + i
            if next_num > n:
                break
            dfs(next_num)

    for i in range(1,10):
        if i > n:
            break
        dfs(i)

    return results