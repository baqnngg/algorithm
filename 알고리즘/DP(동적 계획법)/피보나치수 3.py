n = int(input()) % (15*10**5)
                    #문제에서 M = 1000000 = 10**6 이니까 K = 5
                    #피사노 주기 = 15*10**K (k>2) = 1500000
dp = [0]*(n+1)
dp[1] = 1

for i in range(2,n+1):
    #1,000,000으로 나눈 나머지를 구해서 바로 저장
    dp[i] = (dp[i-1]+dp[i-2]) % 1000000

print(dp[n])