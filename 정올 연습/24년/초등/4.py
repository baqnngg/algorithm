#상자 쌓기 (쌤 풀이)

import sys
# 큰 값으로 초기화 (정답 후보 중 최소값을 찾기 위함)
res = sys.maxsize

# 입력 받기
n = int(input())
arr = list(map(int, input().split()))

for i in range(max(arr)):
    l = 0  # i보다 작은 칸들을 i로 만들기 위해 필요한 추가 작업 수
    r = 0  # i보다 큰 칸들을 i로 만들기 위해 필요한 제거 작업 수

    # 각 칸에 대해 차이를 계산
    for j in range(n):
        if arr[j] >= i:
            r += arr[j] - i  # 상자가 많은 경우: 제거 작업
        else:
            l += i - arr[j]  # 상자가 부족한 경우: 추가 작업

    # 이동으로 처리 가능한 경우도 있으므로 max(l, r)가 필요한 정리 횟수
    # 예를 들어 max(3, 5) -> 3개를 옮기고 2개는 제거하므로 3번
    # 또다른 예로 max(5, 3) -> 3개를 옮기고 2개는 추가하므로 3번
    res = min(res, max(l, r))

# 정답 출력: 가능한 정리 방법 중 최소 횟수
print(res)
