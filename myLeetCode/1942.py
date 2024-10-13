ransomNote = "aaaaaa"
magazine = "aab"
dicransom = {}
for i in ransomNote:
    if i in dicransom:
        dicransom[i] += 1
    if i not in dicransom:
        dicransom[i] = 1
