def has_good_subarray(nums, k):

    if not nums:
        return False

    sum = 0
    remainders = {}

    for num in nums:
        sum += num
        print(sum)
        remainder = sum % k
        print(remainder)


        if remainder == 0 or remainder in remainders:
            print("True with this remainder: ", remainder)
            return True

        remainders[remainder] = True
        print(remainders)

    return False

nums = [5, 12, 7, 17, 8]
k = 10

print(has_good_subarray(nums, k))