A= [1,2,3,4,5,6,7,8]
x = 6

def func (A,x):
    if len(A) == 0:
        return None
    if len(A) ==1 :
        if A[0]>x:
            return 1
        else:
            return 0
    left = A[]