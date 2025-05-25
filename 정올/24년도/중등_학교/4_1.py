import sys
input = sys.stdin.readline

n = int(input().strip())
heights = list(map(int, input().strip().split()))

# 산사태 영향 범위 계산을 위한 리스트 초기화
left_span = [1] * n
right_span = [1] * n

# 왼쪽에서 오른쪽으로 이동하며 영향 범위 계산
for i in range(1, n):
    if heights[i] >= heights[i - 1]:
        left_span[i] = left_span[i - 1] + 1

# 오른쪽에서 왼쪽으로 이동하며 영향 범위 계산
for i in range(n - 2, -1, -1):
    if heights[i] >= heights[i + 1]:
        right_span[i] = right_span[i + 1] + 1

max_span = 0
for i in range(n):
    max_span = max(max_span, left_span[i] + right_span[i] - 1)

print(max_span)
