def letter_combinations(digits):
    if not digits:
        return []

    # Mapping of digits to corresponding letters
    digit_to_char = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    # Backtracking function to generate combinations
    def backtrack(index, path):
        if index == len(digits):
            combinations.append("".join(path))
            return
        possible_chars = digit_to_char[digits[index]]
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
