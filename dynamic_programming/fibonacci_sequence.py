def fibonacci(n, memo=None):
    if memo is None:
        memo = [None] * (n + 1)
    if n == 0:
        return 0
    if n == 2 or n == 1:
        return 1

    if memo[n] is not None:
        return memo[n]

    res = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    print(memo)
    memo[n] = res
    return res


print(fibonacci(20))

def fibonacci_iterative(n):
    if n == 1 or n == 2:
        return 1

    arr = [1, 1]
    sum = 0

    while n - 2 > 0:
        sum = arr[0] + arr[1]
        arr[0] = arr[1]
        arr[1] = sum
        n -= 1

    return sum



print(fibonacci_iterative(20))