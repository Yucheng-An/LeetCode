need, window = {}, {}
t = "Special cossssssunsel Jack Smith provides fullest picture yet of his 2020 election case against Trump in new filing"
t = t.lower()
result = ""
for c in t:
    if c != ' ':
        result += c

for c in result:
    need[c] = need.get(c, 0) + 1
print(need)

print(float('inf'))