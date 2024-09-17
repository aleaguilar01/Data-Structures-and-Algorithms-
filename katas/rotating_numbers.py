def rotating_numbers(n):
    counter = 0

    def helper(num):
        rotated_number = ""
        for digit in str(num):
            if digit == "2" or digit == "3" or digit == "4" or digit == "5" or digit == "7":
                return 0
            elif digit == "6":
                rotated_number = "9" + rotated_number
            elif digit == "9":
                rotated_number = "6" + rotated_number
            else:
                rotated_number = digit + rotated_number

        if str(num) != rotated_number:
            return 1
        return 0

    for number in range(1, n+1):
        counter += helper(number)
    return counter

print(rotating_numbers(30))



