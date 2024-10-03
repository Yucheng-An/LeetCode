need, window = {}, {}
t = "Special counsel Jack Smith provides fullest picture yet of his 2020 election case against Trump in new filing"
for c in t:
    need[c] = need.get(c, 0) + 1
    print(need[c])
print(need)