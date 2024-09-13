def is_balanced(str):
    stack = []
    for char in str:
        if char == "(" or char == "[":
            stack.append(char)

        else:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if top == "[" and char != "]" or top == "(" and char != ")":
                return False

    return len(stack) == 0

#print(is_balanced("()"))
#print(is_balanced("()[()]"))
#print(is_balanced("()]"))
#print(is_balanced("[()"))
print(is_balanced("([)]"))


def is_balanced_not_stack(str):
    counter = 0
    for char in str:
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1
        elif char == "[":
            counter += 2
        elif char == "]":
            counter -= 2

        if counter < 0:
            return False

    return counter == 0

print(is_balanced_not_stack("()"))
print(is_balanced_not_stack("()[()]"))
print(is_balanced_not_stack("()]"))
print(is_balanced_not_stack("[()"))




