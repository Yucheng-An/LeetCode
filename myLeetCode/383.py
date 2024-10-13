def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    dicMagazine = {}
    for i in magazine:
        if i in dicMagazine:
            dicMagazine[i] += 1
        if i not in dicMagazine:
            dicMagazine[i] = 1
    for i in ransomNote:
        if i in dicMagazine:
            dicMagazine[i] -= 1
        if dicMagazine[i] == -1:
            return False
        else:
            return False
     return True
