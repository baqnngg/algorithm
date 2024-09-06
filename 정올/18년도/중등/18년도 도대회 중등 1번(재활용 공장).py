# 내꺼
# import sys
# input = sys.stdin.readline
# n,m = map(int,input().split())
# tra = [[0]*i for i in range(1,n+1)]
# while m >= 0:
#     for i in range(len(tra)):
#         if m - len(tra[i]) < 0:
#             print(m)
#             sys.exit()
#         if m == 0:
#             print(0)
#             sys.exit()
#         m -= len(tra[i])

# 쌤꺼 ###################################################
import sys
# [설계1] 입력 받기
n, m = map(int, input().split())
sum = 0 # 버려진 쓰레기 합
# [설계2] 로봇 멈추기
while sum <= m:
    for i in range(1, n+1):
        sum += i
        if sum > m: # 로봇이 멈추는 순간
            answer = m - (sum - i) # 남겨진 쓰레기 수 계산하기
            break
        
# [설계3] 정답 출력
print(answer)