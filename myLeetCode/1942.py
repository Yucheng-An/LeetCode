ransomNote = "aaaaaa"
magazine = "aab"
dicRansomNote = {}
for i in ransomNote:
    if i in dicRansomNote:
        dicRansomNote[i] += 1
    if i not in dicRansomNote:
        dicRansomNote[i] = 1
