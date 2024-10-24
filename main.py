def minCostSchedule(n, s, r, c):
    # Initialize the DP array to store minimum costs up to each week
    OPT = [float('inf')] * (n + 1)

    # Base cases
    OPT[0] = 0  # No weeks, no cost
    if n >= 1:
        OPT[1] = r * s[0]  # Cost for week 1
    if n >= 2:
        OPT[2] = r * s[0] + r * s[1]  # Cost for first two weeks
    if n >= 3:
        OPT[3] = r * s[0] + r * s[1] + r * s[2]  # Cost for first three weeks

    # Fill the DP table from week 4 to week n
    for i in range(4, n + 1):
        # Option 1: Use Company A for week i
        optionA = r * s[i - 1] + OPT[i - 1]

        # Option 2: Use Company B for the block ending at week i
        optionB = float('inf')
        if 4 <= i:
            optionB = c * 4 + OPT[i - 4]

        # Choose the minimum of the two
        OPT[i] = min(optionA, optionB)

    return OPT[n]

# Example Usage:
n = 10
s = [11, 9, 9, 12, 12, 12, 12, 9, 9, 11]   # Weekly supply in pounds
r = 1  # Cost per pound for Company A
c = 10  # Fixed weekly cost for Company B

min_cost = minCostSchedule(n, s, r, c)
print(f"Minimum cost: {min_cost}")
