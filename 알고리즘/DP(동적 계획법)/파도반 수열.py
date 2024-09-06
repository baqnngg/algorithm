# [설계1] 입력받기
a = int(input())
b = []
dp = [0] * 10000

for i in range(a):
    b.append(int(input()))

dp[1],dp[2],dp[3],dp[4],dp[5] = 1,1,1,2,2

# [설계2] dp채우기?
for i in range(6,max(b)+1):
    dp[i] = dp[i-1] + dp[i-5]

# [설계3] 출력하기
for i in range(len(b)):
    print(dp[b[i]])