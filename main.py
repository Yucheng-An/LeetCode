from logging import raiseExceptions


def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    pass


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    strList = []
    for i in range(min_factor, max_factor + 1):
        strList.append(str(i))
    print(strList)
    palindromeList = []
    for i in strList:
        stack = []
        for j in range(0, len(i) // 2 + 1):
            stack.append(i[j])
        for j in range(len(i) // 2, len(i)):
            if i[j] == stack[-1]:
                stack.pop(-1)
            elif i[j] != stack[-1]:
                stack = []
                break
            if stack is None:
                palindromeList.append(i)
                stack = []
    print(palindromeList)

def checkPalindrome(s):
    stack = []
    for i in range(0,len(s)//2):
        stack.append(s[i])
    print(stack)
    for i in range(len(s)//2,len(s)):
        if stack[-1] != s[i]:
            pass
        else:
            stack.pop()
    print(stack)
    if stack is None:
        return True
        
s="12345"
print(s[:])
print(checkPalindrome("11111"))
print("--------")
smallest(1, 9)
