def letterCombinations(digits):
    # 23
    keyboard = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
    subKeyboar = []
    allCombine = []
    for i in range(len(digits)):
        for j in keyboard[int(digits[i])]:
            print(j)
