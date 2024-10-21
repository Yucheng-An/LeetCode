def lengthLongestPath( input):
    stack = []
    max_len = 0
    for part in input.split("\n"):
        level = part.rfind("\t") + 1
        while level < len(stack):
            stack.pop()
        stack.append(len(part) - level)
        if "." in part:
            total_length = sum(stack) + len(stack) - 1
            # 加上父路径的分隔符
            max_len = max(max_len, total_length)
    return max_len
