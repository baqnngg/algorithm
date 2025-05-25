import sys

# [1] 입력 받기
n, m = map(int, input().split())

cylinders = []
all_numbers = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    cylinders.append((a, b))
    all_numbers.append(a)
    all_numbers.append(b)

# [2] 중복 제거, 정렬
all_numbers = sorted(list(set(all_numbers)))

# 각 숫자에 대하여 반대쪽 숫자의 집합 저장
number_connections = {}
for num in all_numbers:
    number_connections[num] = set()

for a, b in cylinders:
    number_connections[a].add(b)
    number_connections[b].add(a)

# [3] 질문 처리하기
for _ in range(m):
    s = int(sys.stdin.readline())
    result = 0
    
    # 모든 숫자에 대해 확인
    for j in all_numbers:
        # j와 연결된 모든 숫자 k에 대해 확인
        for k in number_connections[j]:
            # s-k가 j와도 연결되어 있는지 확인
            if s-k in number_connections[j]:
                # k와 s-k가 같으면 건너뛰기 (자기 자신과 연결할 수 없음)
                if k == s-k:
                    continue
                result += 1
    
    # 각 쌍이 두 번 카운트되므로 2로 나눔
    print(result // 2)