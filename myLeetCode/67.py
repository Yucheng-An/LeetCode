def addBinary(a,b):
    maxlengh = max(len(a),len(b))
    a = a.zfill(maxlengh)
    b = b.zfill(maxlengh)
    carry = 0
    res = []
    for i in range(maxlengh-1,-1,-1):
        inta = int(a[i])
        intb = int(b[i])
        total = inta + intb + carry
        res.append(str(total%2))
        carry = total//2
    if carry:
        res.append('1')
    return ''.join(reversed(res))

a = "11"
b = "1"
res = addBinary(a,b)
print(res)
print(1//2)