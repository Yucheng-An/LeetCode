def addBinary(a,b):
    t = ''
    for i in range(abs(len(a)-len(b))):
        t = t + '0'
    if len(a)>len(b):
        fullB = t + b
        fullA = a
    elif len(b) > len(a):
        fullA = t + a
        fullB = b

    
    



a = "11"
b = "1"
res = addBinary(a,b)
print(res)