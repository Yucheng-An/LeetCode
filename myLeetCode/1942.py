ransomNote = "aa"
magazine = "aab"
dicRansomNote = {}
dicMagazine = {}
for i in magazine:
    if i in dicRansomNote:
        dicRansomNote[i] += 1
    if i not in dicRansomNote:
        dicRansomNote[i] = 1
for