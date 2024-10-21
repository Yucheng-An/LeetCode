def strStr(haystack: str, needle: str) -> int:
    if len(haystack) < len(needle):
        return -1
    h = 0
    while h < len(haystack):
        t = h
        for n in range(len(needle)):
            if needle[n] == haystack[t]:
                if n == len(needle) - 1:
                    return h
                else:
                    t += 1
            else:
                break
        h+=1
    return -1

