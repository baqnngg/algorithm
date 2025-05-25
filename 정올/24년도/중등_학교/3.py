n = int(input())
arr = list(map(int, input().split()))
m = 0

for i in range(len(arr) - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            m += 1
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
print(m)