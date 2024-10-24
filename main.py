def minCostSchedule(weekNumber, supplyList, companyA_Rate, companyB_):
    OPT = [float('inf')] * (weekNumber + 1)
    OPT[0] = 0
    if weekNumber >= 1:
        OPT[1] = companyA_Rate * supplyList[0]
    if weekNumber >= 2:
        OPT[2] = companyA_Rate * supplyList[0] + companyA_Rate * supplyList[1]
    if weekNumber >= 3:
        OPT[3] = companyA_Rate * supplyList[0] + companyA_Rate * supplyList[1] + companyA_Rate * supplyList[2]
    for i in range(4, weekNumber + 1):
        optionA = companyA_Rate * supplyList[i - 1] + OPT[i - 1]
        optionB = float('inf')
        if 4 <= i <= weekNumber-4:
            optionB = companyB_ * 4 + OPT[i - 4]
        OPT[i] = min(optionA, optionB)
    return OPT[weekNumber]

# Example Usage:
n = 10
s = [11, 9, 9, 12, 12, 12, 12, 9, 9, 11]   # Weekly supply in pounds
r = 1  # Cost per pound for Company A
c = 10  # Fixed weekly cost for Company B

min_cost = minCostSchedule(n, s, r, c)
print(f"Minimum cost: {min_cost}")
