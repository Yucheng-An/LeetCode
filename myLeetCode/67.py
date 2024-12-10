def addBinary(a,b):
    maxlengh = max(len(a),len(b))
    a = a.zfill(maxlengh)
    b = b.zfill(maxlengh)
    print(a)
    print(b)
    
    



a = "11"
b = "1"
res = addBinary(a,b)
print(res)