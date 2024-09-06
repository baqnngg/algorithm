def solution(arr):
    left, right = 0, len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
arr = [1, 4, 2, 3]
ret = solution(arr)
print("Solution: return value of the function is ", ret, " .")