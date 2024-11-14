def letter_combinations(digits):
    if not digits:
        return []
    keyboard = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

    def backtrack(index, path):
        keyboard = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                    ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        if index == len(digits):
            combinations.append("".join(path))
            return
        possible_chars = keyboard[int(digits[index])]
        for char in possible_chars:
            path.append(char)
            backtrack(index + 1, path)
            path.pop()  # backtrack

    combinations = []
    backtrack(0, [])
    return combinations


# Example usage
digits = "23"
print(letter_combinations(digits))
