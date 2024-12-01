A = [1, 2, 3, 4, 5, 6, 7, 8]
x = 6


def func(A, x):
    if len(A) == 0:
        return None
    if len(A) == 1:
        return 1 if A[0] > x else 
    left = A[:len(A) // 2]
    right = A[len(A) // 2:]
    return right + left


res = func(A, x)
print(res)
