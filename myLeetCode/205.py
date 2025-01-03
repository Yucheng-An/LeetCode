def isIsomorphic(s: str, t: str) -> bool:
    # Create dictionaries to store the mappings
    map_s_to_t = {}
    map_t_to_s = {}

    for char_s, char_t in zip(s, t):
        # Check s -> t mapping
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                return False
        else:
            map_s_to_t[char_s] = char_t

        # Check t -> s mapping
        if char_t in map_t_to_s:
            if map_t_to_s[char_t] != char_s:
                return False
        else:
            map_t_to_s[char_t] = char_s

    return True








s = "egg"
t = "add"
isIsomorphic(s,t)
# 
# smap = {}
# tmap = {}
# for c in s:
#     if c not in smap:
#         smap[c] = 1
#     else:
#         smap[c] += 1
# for c in t:
#     if c not in tmap:
#         tmap[c] = 1
#     else:
#         tmap[c] += 1
# 
# print(smap)
# print(tmap)