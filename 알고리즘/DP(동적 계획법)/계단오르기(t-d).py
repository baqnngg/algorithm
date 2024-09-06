# [설계1] 입력 받기
num = int(input())
dp = [0] * 21
# [설계2] 계단 오르는 횟수 계산(DP: Top-Down 방식)
def stair(n):
    if dp[n] != 0:
        return dp[n]
    dp[n] = stair(n-1) + stair(n-2)# memoization (점화식)
    return dp[n]
# [설계3] 정답 출력
dp[1] = 1
dp[2] = 2

print(stair(num))