# b-t방식
#[설계1] 입력받기
num = int(input())

#[설계2] dp받기
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
#[설계3] 오른횟수 구하기
for i in range(3,num+1):
    dp[i] = dp[i-1] + dp[i-2]

#[설계4] 출력-
print(dp[num]%10007)

# ------------------------------------------------

#t-d방식
# [설계1] 입력 받기
num = int(input())
dp = [0] * 1001
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