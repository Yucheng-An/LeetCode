def canCompleteCircuit(gas, cost):
    totalgas = 0
    totalcost = 0
    currencost = 0
    startstation = 0
    for i in range(len(gas)):
        totalgas += gas[i]
        totalcost += cost[i]
        currencost = totalgas - totalcost
        if currencost < 0:
            startstation = i+1
            currencost = 0
    return startstation-1

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas,cost))