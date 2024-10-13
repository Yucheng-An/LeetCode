def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    dicRansomNote = {}
        for i in magazine:
            if i in dicMagazine:
                dicMagazine[i] += 1
            if i not in dicMagazine:
        dicMagazine[i] = 1
print(dicMagazine)
for i in ransomNote:
    if i in dicMagazine:
        dicMagazine[i] -= 1
        if dicMagazine[i] == -1:
            return False
    else:
        return False
return True
