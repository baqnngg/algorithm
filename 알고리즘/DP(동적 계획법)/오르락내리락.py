# [설계1] 입력받기
n = int(input())
dt = list(map(int,input().split()))

# [설계2] 가장 길게 증가하는 부분의 길이 구하기
dp1 = [1] * n
for i in range(n):
    for j in range(i):
        if dt[i] > dt[j]:
            dp1[i] = max(dp1[i],dp1[j]+1)
# [설계3] 가장 길게 감소하는 부분의 길이 구하기(= 위에 것을 역순으로 하는 방법...)
dp2 = [1] * n
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if dt[i] > dt[j]:
            dp2[i] = max(dp2[i],dp2[j]+1)
# [설계4] 길게 증가하는 부분과 감소하는 부분 합치기
ans = -1
for i in range(n):
    ans = max(dp1[i]+dp2[i],ans) # 최대값 구하기
# [설계5] 정답 출력
print(ans-1)