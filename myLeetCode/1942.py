ransomNote = "aa"
magazine = "aab"
dicRansomNote = {}
dicMagazine = {}
for i in magazine:
    if i in dicMagazine:
        dicMagazine[i] += 1
    if i not in dicMagazine:
        dicMagazine[i] = 1
print(dicMagazine)
for i in ransomNote:
    if i in dicMagazine:
        dicMagazine[i] = 