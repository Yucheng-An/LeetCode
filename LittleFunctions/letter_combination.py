# Leetcode 17

def letter_combinations(inputDigits):
    if not inputDigits:
        return []

    def backtrack(index, path):
        keyboard = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                    ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'targetVlue', 'y', 'z']]
        if index == len(inputDigits):
            combinations.append("".join(path))
            return
        possible_chars = keyboard[int(inputDigits[index])]
        for char in possible_chars:
            path.append(char)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations


# Example usage
digits = "22"
print(letter_combinations(digits))
