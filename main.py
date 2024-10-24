def minCostSchedule(weekNumber, supplyList, companyARate, c):
    OPT = [float('inf')] * (weekNumber + 1)
    OPT[0] = 0
    if weekNumber >= 1:
        OPT[1] = companyARate * supplyList[0]
    if weekNumber >= 2:
        OPT[2] = companyARate * supplyList[0] + companyARate * supplyList[1]
    if weekNumber >= 3:
        OPT[3] = companyARate * supplyList[0] + companyARate * supplyList[1] + companyARate * supplyList[2]
    for i in range(4, weekNumber + 1):
        optionA = companyARate * supplyList[i - 1] + OPT[i - 1]
        optionB = float('inf')
        if 4 <= i <= weekNumber-4:
            optionB = c * 4 + OPT[i - 4]
        OPT[i] = min(optionA, optionB)
    return OPT[weekNumber]

# Example Usage:
n = 10
s = [11, 9, 9, 12, 12, 12, 12, 9, 9, 11]   # Weekly supply in pounds
r = 1  # Cost per pound for Company A
c = 10  # Fixed weekly cost for Company B

min_cost = minCostSchedule(n, s, r, c)
print(f"Minimum cost: {min_cost}")
