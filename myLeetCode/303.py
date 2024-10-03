need, window = {}, {}
t = "hello"
for c in t:
    need[c] = need.get(c, 0) + 1
print(need)