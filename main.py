
def count_greater(A, x):
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return 1 if A[0] > x else 0
    left = A[:len(A) // 2]
    right = A[len(A) // 2:]
    
    return count_greater(left,x) + count_greater()

A = [1, 2, 3, 4, 5, 6, 7, 8]
x = 6
res = count_greater(A, x)
print(res)
