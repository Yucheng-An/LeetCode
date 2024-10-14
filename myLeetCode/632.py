def find (il):
    if len(il) == 1:
        return None
    if il[0]-il[1]==-1:
        il.pop()
        find(il)
    else:
        return il[1]-1

t = [0,1,3,4,5,]