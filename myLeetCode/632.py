def find(il):
    if len(il) == 1:
        return None
    if il[-1] - il[-2] == 1:
        il.pop()
        find(il)
    else:
        res = il[-1] - 1
        return res


t = [0, 1, 3, 4, 5, 6]
print(t[-2])
res = find(t)
print(res)
print(t[-1])