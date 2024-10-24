def minCostSchedule(n, s, r, c):
    OPT = [float('inf')] * (n + 1)
    OPT[0] = 0
    if n >= 1:
        OPT[1] = r * s[0]
    if n >= 2:
        OPT[2] = r * s[0] + r * s[1]
    if n >= 3:
        OPT[3] = r * s[0] + r * s[1] + r * s[2]
    for i in range(4, n + 1):
        optionA = r * s[i - 1] + OPT[i - 1]
        optionB = float('inf')
        if 4 <= i <= n-4:
            optionB = c * 4 + OPT[i - 4]
        OPT[i] = min(optionA, optionB)
    return OPT[n]

# Example Usage:
n = 10
s = [11, 9, 9, 12, 12, 12, 12, 9, 9, 11]   # Weekly supply in pounds
r = 1  # Cost per pound for Company A
c = 10  # Fixed weekly cost for Company B

min_cost = minCostSchedule(n, s, r, c)
print(f"Minimum cost: {min_cost}")
