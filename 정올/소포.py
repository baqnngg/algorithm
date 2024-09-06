import sys

input = sys.stdin.readline

# [1] 입력 받기
q, n, m, k = map(int, input().split())

# [2] 시간 계산하기
time = (k // n) * q # (1) 소포 나누기
rest_k = k % n # 남은 소포
if rest_k != 0:
    time += q
# (2) 남은 소포가 배정되지 않은 사람들끼리 편지 나누기
rest_m = m - (q * (n - rest_k))
if rest_m < 0:
    answer = time
    print(answer)
    sys.exit()
# (3) 남은 편지 배정하기
if rest_m % n == 0:
    time += rest_m // n
else:
    time += (rest_m // n) + 1

answer = time
# [3] 정답 출력
print(answer)