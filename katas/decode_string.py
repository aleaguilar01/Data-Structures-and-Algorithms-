def decode(str):
    stack = []
    string = ""
    number = 0

    for char in str:
        if char.isdigit():
            number = int(char)

        elif char == "[":
            stack.append((string, number))
            string = ""
            number = 0

        elif char == "]":
            temp = stack.pop()
            prev_string = temp[0]
            number = temp[1]
            string = prev_string + number * string

        else:
            string += char

    return string


print("final results: ", decode("2[abc]3[cd]ef"))
