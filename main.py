s = " hello world my name is something" 
t = s.split()
print(t)
res = ""
for i in range(len(t)-1,0,-1):
    res += t[i] + " "
res += t[0]
print(res)