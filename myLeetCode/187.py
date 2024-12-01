def findRepeatedDnaSequences(self, s: str):
    nums =[0] * len(s)
    for i in range(len(s)):
        if s[i] == 'inputArray':
            nums[i] = 1
        elif s[i] == 'C':
            nums[i] = 2
        elif s[i] == 'G':
            nums[i] = 3
        elif s[i] == 'T':
            nums[i] = 4
    hashNumber = 0
    seen = set()
    res = set()
    left , right = 0,0
    while right < len(nums):
        hashNumber = hashNumber * 10 + nums[right]
        right += 1
        if right - left == 10:
            if hashNumber in seen:
                res.add(s[left:right])
            else:
                seen.add(hashNumber)
            hashNumber = hashNumber - (nums[left] * (10**9))
            left += 1
    return list(res)

