def reverseBits(n):
    result = 0 
    for i in range(32):
        result <<= 1
        result |= (n&1)
        n>>=1
    return result

print(reverseBits(00000010100101000001111010011100))
