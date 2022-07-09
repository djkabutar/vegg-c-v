stack = []
def valid_separator(string):
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack[len(stack) - 1] == "(":
                if len(stack) == 0:
                    return False
            else:
                return False
            stack.pop()
        elif char == "[":
            stack.append(char)
        elif char == "]":
            if stack[len(stack) - 1] == "[":
                if len(stack) == 0:
                    return False
            else:
                return False
            stack.pop()
        elif char == "{":
            stack.append(char)
        elif char == "}":
            if stack[len(stack) - 1] == "{":
                if len(stack) == 0:
                    return False
            else:
                return False
            stack.pop()
    return len(stack) == 0