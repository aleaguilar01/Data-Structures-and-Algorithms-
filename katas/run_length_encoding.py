def runLengthEncoding(string):
    counter = 0
    current = string[0]
    index = 0
    final_string = ""

    print(len(string))

    while index < len(string):
        substring = current
        if string[index] == current and counter < 9:
            counter += 1
            index += 1
        else:
            final_string += f"{counter}{substring}"
            current = string[index]
            counter = 0

    final_string += f"{counter}{substring}"

    return final_string

print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))