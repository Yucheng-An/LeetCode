def find (il):
    if len(il) == 1:
        return None
    if il[0]-il[1]==-1:
        il.pop()
        find(il)
    else:
        return list[1]-1