# [설계1] 입력 받기
N = int(input())
# [설계2] N을 1로 만드는 방법의 최소값 구하기(Dynamic Programming, Bottom-Up)
for _ in range(N):
    k = int(input())
    n = int(input())

    dp = [0]*n
    dp[0] = 1
    for i in range(1,n): #dp 초기화
        dp[i] += (dp[i-1]+1)

    for _ in range(k): #층
        for i in range(1,n): #호
            dp[i] += dp[i-1]
    print(dp[-1])