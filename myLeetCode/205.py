def isIsomorphic(s, t):
    smap = {}
    tmap = {}
    pass










s = "egg"
t = "add"

smap = {}
for c in s:
    if c not in smap:
        smap.append(c)
        smap[c] = 1
    else:
        smap[c] += 1
