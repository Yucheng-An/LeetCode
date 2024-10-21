print(abs(-10))

def t (s):
    res = 0
    for i in range(len(s)):
        if s[i] == '(':
            res += 1
        elif s[i] == ')':
            res -= 1
    return abs(res)
    
print(t("((("))