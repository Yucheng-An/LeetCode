need, window = {}, {}
t = "Special counsel Jack Smith provides fullest picture yet of his 2020 election case against Trump in new filing"
result = ""
for c in t:
    if c != ' ':
        result += c

for c in result:
    need[c] = need.get(c or , 0) + 1
print(need)
