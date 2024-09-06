# [설계1] 입력 받기
N = int(input())
dp = [0] * (1000001)
# [설계2] N을 1로 만드는 방법의 최소값 구하기(Dynamic Programming, Bottom-Up)
dp[1] = 0 # 초기값 설정
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1 # 1을 빼는 경우
    if i % 3 == 0: # 3으로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i//3]+1) # 1 빼는 경우 VS 3으로 나누는 것 중 최소 횟수로 업데이트하기
    if i % 2 == 0: # 2로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i//2]+1) # 1 빼는 경우 VS 2로 나누는 것 중 최소 횟수로 업데이트하기
# [설계3] 정답 출력
print(dp[N])