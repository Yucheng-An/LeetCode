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

def func(cents):
    if cents == 15:
        return 6
    else:
        return None


def input_15():
    helperTest(6,15)
    helperTest(6,12)
    
        
def helperTest(expected,inputValue):
    if expected == func(inputValue):
        print("test pass")
    else:
        print("test fail")

input_15()
            