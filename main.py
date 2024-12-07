# 
# There are four types of common coins in US currency:
# o) quarters (25 cents)
# o) dimes (10 cents)
# o) nickels (5 cents)
# o) pennies (1 cent)
# 
# There are 6 ways to make change for 15 cents:
# o) A dime and a nickel;
# o) A dime and 5 pennies;
# o) 3 nickels;
# o) 2 nickels and 5 pennies;
# o) A nickel and 10 pennies;
# o) 15 pennies.
# 
# How many ways are there to make change for a dollar using these common coins? (1 dollar = 100 cents).
# 
# [Source http://rosettacode.org]

def func(total,default = [1,5,10,25] coins):
    dp = [0] * (total + 1)
    dp[0] = 1  # Base case: one way to make 0 cents

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = dp[x] + dp[x - coin]
    return dp[total]

coins = [1,5,10,25]
total = 15
print(func(15,coins))
