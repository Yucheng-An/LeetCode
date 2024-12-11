def change(amount,coins):
    dp = [0] * (amount+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] += dp[i-coin]
    return dp[amount]


coin = [1,5,10,25]
amount = 12
print(change(amount,coin))