def change(amount,coins):
    dp = [0] * (amount+1)
    dp[0] = 1
    for 