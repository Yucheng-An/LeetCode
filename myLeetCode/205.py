def isIsomorphic(s, t):
    smap = {}
    tmap = {}
    pass










s = "egg"
t = "add"

smap = {}
tmap = {}
for c in s:
    if c not in smap:
        smap[c] = 1
    else:
        smap[c] += 1
for c in t:
    if c not in smap:
        tmap[c] = 1
    else:
        tmap[c] += 1
print(smap)
print(tmap)