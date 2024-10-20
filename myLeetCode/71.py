def simplifyPath(path):
    parts = path.split("/")
    stk = []
    for part in parts:
        if part == "" or part == ".":
            continue
        if part == "..":
            if stk:
                stk.pop()
            continue
        stk.append(part)
    res = ""
    while stk:
        res = "/" + stk.pop() + res
    return res if res else "/"


print(simplifyPath("/.../a/../b/c/../d/./"))