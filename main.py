def letterCombinations(digits):
    # 23
    keyboard = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
    subKeyboard = []
    allCombine = []
    for i in range(len(digits)):
        subKeyboard.append(keyboard[int(digits[i])])
    print(subKeyboard)
    for i in range(len(subKeyboard)):
        
    
    

letterCombinations("23")