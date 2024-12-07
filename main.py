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


def func(total, coins):
    dp = [0] * (total + 1)
    dp[0] = 1 
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = dp[x] + dp[x - coin]
    return dp[total]


total = 10
print(func(total, [1, 5, 10, 25]))
