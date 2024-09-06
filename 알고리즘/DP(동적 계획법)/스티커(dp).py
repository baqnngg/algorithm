T = int(input())
for i in range(T):
    n = int(input())
    sticker = [0]*2

    # 스티커점수 받기
    for i in range(2):
        sticker[i] = list(map(int,input().split()))
    
    # dp채우기
    dp = [[0] * n for _ in range(2)]

    # dp초기화
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    # 스티커가 한줄일때
    if n == 1:
        print(max(dp[0][0],dp[1][0]))
        continue

    dp[0][1] = sticker[1][0] + sticker[0][1]
    dp[1][1] = sticker[0][0] + sticker[1][1]

    if n == 2:
        print(max(dp[0][1],dp[1][1]))
        continue

    for i in range(2,n):
        dp[0][i] = max(dp[1][i-2],dp[1][i-1]) + sticker[0][i]
        dp[1][i] = max(dp[0][i-2],dp[0][i-1]) + sticker[1][i]

    print(max(dp[0][n-1],dp[1][n-1]))