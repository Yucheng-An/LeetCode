def find(il):
    if len(il) == 1:
        return None
    if il[-1] - il[-2] == 1:
        il.pop()
        find(il)
    else:
        return il[-1] - 1


t = [0, 1, 3, 4, 5, 6]
print(t.pop())
