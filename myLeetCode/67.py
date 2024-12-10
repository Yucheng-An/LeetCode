def addBinary(a,b):
    t = None
    for i in range(abs(len(a)-len(b))):
        t += '0'
    if len(a)>len(b):
        fullB = t + b
        fullA = a
    elif len(b) > len(a):
        fullA = t + a
        fullB = b
    print(fullA)
    print(fullB)
        
    
    



a = "11"
b = "1"
res = addBinary(a,b)
print(res)