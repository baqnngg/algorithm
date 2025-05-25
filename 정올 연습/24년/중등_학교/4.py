# 산사태
n = int(input())
h = list(map(int,input().split()))
rh = [1] * n
lh = [1] * n
for i in range(n-1):
    if h[i] <= h[i+1]:
        rh[i+1] = rh[i] + rh[i+1]
for i in range(n-1, 0, -1):
    if h[i] <= h[i-1]:
        lh[i-1] = lh[i] + lh[i-1]
m = 0
for i in range(n):
    m = max(m, rh[i] + lh[i] - 1)
print(m)