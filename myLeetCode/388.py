def lengthLongestPath( input) -> int:
    # 这个栈存储之前的父路径。实际上这里只用存父路径的长度就够了，这个优化留给你吧
    stack = []
    max_len = 0
    for part in input.split("\n"):
        level = part.rfind("\t") + 1
        # 让栈中只保留当前目录的父路径
        while level < len(stack):
            stack.pop()
        stack.append(len(part) - level)
        # 如果是文件，就计算路径长度
        if "." in part:
            total_length = sum(stack) + len(stack) - 1
            # 加上父路径的分隔符
            max_len = max(max_len, total_length)
    return max_len