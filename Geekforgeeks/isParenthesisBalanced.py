def isParenthesisBalanced(s):
    stack = []
    for i in s:
        if i == '{':
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == '{' and stack[-1] == '}':
            stack.pop()
        elif i == '(' and stack[-1] == ')':
            stack.pop()
        elif i == '[' and stack[-1] == ']':
            stack.pop()
        elif len(stack) == 0:
            pass
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False


print(isParenthesisBalanced("{([])}"))