def findRepeatedDnaSequences(self, s: str):
    nums =[0] * len(s)
    for i in :
        if s == 'A':
            nums[i] = 1
        elif s == 'C':
            nums[i] = 2
        elif s == 'G':
            nums[i] = 3
        elif s == 'T':
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

