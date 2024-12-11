def change(amount,coins):
    dp = [0] * (amount+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount+1):
            something = dp[i-coin]
            dp[i] += something
    return dp[amount]


coin = [1,5,10,25]
amount = 12
print(change(amount,coin))