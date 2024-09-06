a = int(input())
sco = [0]*301
for i in range(1,a+1):
    sco[i] = int(input())

dp = [0]*301
dp[1] = sco[1]
dp[2] = sco[1]+sco[2]
dp[3] = max(sco[1]+sco[3],sco[2]+sco[3])

for i in range(4,a+1):
    dp[i] = max(dp[i-3]+sco[i-1]+sco[i],dp[i-2]+sco[i])
print(dp[a])