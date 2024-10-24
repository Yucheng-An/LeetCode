def minCostSchedule(weekNumber, supplyList, companyA_Rate, companyB_Amount):
    OPT = [float('inf')] * (weekNumber + 1)
    OPT[0] = 0
    for i in range(1,4):
        OPT[i] = OPT[i-1]
    if weekNumber >= 1:
        OPT[1] = companyA_Rate * supplyList[0]
    if weekNumber >= 2:
        OPT[2] = OPT[1] + companyA_Rate * supplyList[1]
    if weekNumber >= 3:
        OPT[3] = OPT[2] + companyA_Rate * supplyList[2]
    for i in range(4, weekNumber + 1):
        chooseA = companyA_Rate * supplyList[i - 1] + OPT[i - 1]
        chooseB = float('inf')
        if i >= 4:
            chooseB = companyB_Amount * 4 + OPT[i - 4]
        OPT[i] = min(chooseA, chooseB)
    return OPT[weekNumber]

# Example Usage:
n = 10
s = [11, 9, 9, 12, 12, 12, 12, 9, 9, 11]   # Weekly supply in pounds
r = 1  # Cost per pound for Company A
c = 10  # Fixed weekly cost for Company B

min_cost = minCostSchedule(n, s, r, c)
print(f"Minimum cost: {min_cost}")
