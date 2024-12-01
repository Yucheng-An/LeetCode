A = [1, 2, 3, 4, 5, 6, 7, 8]
x = 6

def count_greater(A, x):
    # Base case: If the array is empty, return 0
    if len(A) == 0:
        return 0
    # Base case: If the array has one element, check if it is greater than x
    if len(A) == 1:
        return 1 if A[0] > x else 0
    # Divide the array into two halves
    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]
    # Recursively count in each half
    count_left = count_greater(left, x)
    count_right = count_greater(right, x)
    # Combine the results
    return count_left + count_right

res = count_greater(A, x)
print(res)
