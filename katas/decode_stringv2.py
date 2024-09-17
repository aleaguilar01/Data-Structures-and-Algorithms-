def decode(st):
    stack = []
    result = ""
    for char in st:
        if char.isdigit():
            stack.append(result)
            stack.append(int(char))
            result = ""
        elif char == "[":
            pass
        elif char == "]":
            times = stack.pop()
            sub_result = stack.pop()
            result = sub_result + (int(times) * result)
        else:
            result += char
    return result


print("final results: ", decode("2[ac3[d]]f"))
