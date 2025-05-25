# 룩(Rook) around!
import itertools
import sys

# [1] 입력 받기
n = int(input())
weights = []
for _ in range(n):
    row = list(map(int, input().split()))
    weights.append(row)

# [2] 가중치 합 구하기()
min_sum = sys.maxsize
max_sum = -sys.maxsize

# 모든 가능한 열 배치를 생성 (permutation 활용), row: 행 , col: 열, cols: 룩이 배치된 열들
for cols in itertools.permutations(range(n)):
    # 각 행마다 하나의 룩을 배치
    # cols[i]: i번째 행에서 룩이 위치한 열을 의미
    # 예를 들어 입력이 2
    #                 1 2
    #                 3 4 의 경우
    # itertools.permutations(range(n)) -> (0, 1) / (1, 0)
    # 이 때, (0, 1)에서 0 -> (0행, 0열)에 룩을 놓는 경우, 1 -> (1행 1열에 룩을 놓는 경우)
    # (1, 0)에서 1 -> (0행, 1열)에 룩을 놓는 경우, 0 -> (1행 0열에 룩을 놓는 경우)를 의미함.
    
    # 가중치 합 계산
    weight_sum = 0
    for row in range(n):
        col = cols[row]
        weight_sum += weights[row][col]
    
    # 최소/최대 값 갱신
    min_sum = min(min_sum, weight_sum)
    max_sum = max(max_sum, weight_sum)

# [3] 결과 출력
print(min_sum, max_sum)