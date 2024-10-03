need, window = {}, {}
t = "Special cossssssunsel Jack Smith provides fullest picture yet of his 2020 election case against Trump in new filing"
result = ""
for c in t:
    if c != ' ':
        result += c

for c in result:
    need[c] = need.get(c or ord(c) == ord(c) - 32, 0) + 1
print(need)

print(ord('c')-ord('C'))