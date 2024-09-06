#[설계1] 입력받기
num = int(input())

#[설계2] dp받기
dp = [0] * 21 #숫자가 최대 20개 까지 받을수 있기 때문
dp[1] = 1
dp[2] = 2
#[설계3] 오른횟수 구하기
for i in range(3,num+1):  
    dp[i] = dp[i-1] + dp[i-2]

#[설계4] 출력-
print(dp[num])