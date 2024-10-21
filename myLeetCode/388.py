from tempfile import tempdir


def lengthLongestPath( input):
    stack = []
    max_len = 0
    tempdir=
    for part in input.split("\n"):
        
        level = part.rfind("\t") + 1
        while level < len(stack):
            stack.pop()
        stack.append(len(part) - level)
        if "." in part:
            total_length = sum(stack) + len(stack) - 1
            max_len = max(max_len, total_length)
    return max_len

input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(lengthLongestPath(input))