def canCompleteCircuit(gas, cost):
    totalGas = 0
    totalCost = 0 
    currentBalance = 0
    startStation = 0
    for i in range(len(gas)):
        totalGas += gas[i]
        totalCost += cost[i]
        currentBalance = currentBalance + 


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas, cost))
