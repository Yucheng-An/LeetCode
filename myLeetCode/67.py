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
    aPointer = len(fullA) -1
    bPointer = len(fullB) -1
    carry = 0 
    res = ""
    while aPointer >= 0 and bPointer >= 0:
        if int(a[aPointer]) + int(b[bPointer]) == 2:
            carry = 1
            res = res + "0"
        else:
            carry = 0
            res = res + str(int(a[aPointer]) + int(b[bPointer]))
        
    
    



a = "11"
b = "1"
res = addBinary(a,b)
print(res)