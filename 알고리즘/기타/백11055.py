n = int(input())
dt = list(map(int,input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if dt[i] > dt[j]:
            dp[i] = max(dp[i],dp[j]+1)
ss = [[]]
k = 0
for i in range(len(dp)):
    if dp[i] < dp[i+1]:
        ss[k].append(dt[i+1])
    elif dp[i] == dp[i+1]:
        k += 1
        ss.append([])
        ss[k].append(dt[i+1])
