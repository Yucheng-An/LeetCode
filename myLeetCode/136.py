def canCompleteCircuit(gas, cost):
    totalgas = 0
    totalcost = 0
    currentcost = 0
    startstation = 0
    for i in range(len(gas)):
        totalgas += gas[i]
        totalcost += cost[i]
        currencost = totalgas - totalcost
        if currentcost < 0:
            startstation += 1
            currentcost = 0
    
    
