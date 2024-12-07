def sort012(self, arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            t = arr[low]
            arr[low] = arr[mid]
            arr[mid] = t
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            t = arr[high]
            arr[high] = arr[mid]
            arr[mid] = t
            high -= 1
