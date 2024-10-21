def generateParenthesis(n):
    # dp[i] will store all the combinations of well-formed parentheses with i pairs
    dp = [[] for _ in range(n + 1)]
    res = []
    # Base case: there's only one combination with 0 pairs of parentheses
    dp[0] = [""]

    # Fill the dp array for each number of pairs from 1 to n
    for i in range(1, n + 1):
        current_combinations = []
        for p in range(i):
            q = i - 1 - p
            for left in dp[p]:
                for right in dp[q]:
                    current_combinations.append(f"({left}){right}")
                    res.append(f"({left}){right}")
        dp[i] = current_combinations

    return dp

# Example usage:
n = 3
print(generateParenthesis(n))
