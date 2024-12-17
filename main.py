s = " hello world my name is something" 
t = s.split()
print(t)
res = ""
for i in range(len(t)-1,-1,-1):
    res += 