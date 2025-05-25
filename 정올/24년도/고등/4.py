import sys
n, m = map(int, input().split())
arr = []
dict = {}
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append(a)
    arr.append(b)
    if a not in dict:
        dict[a] = {}
    if b not in dict:
        dict[b] = {}
    if b not in dict[a]:
        dict[a][b] = 1
    if a not in dict[b]:
        dict[b][a] = 1
arr.sort()
arr = list(set(arr))
for i in range(m):
    s = int(sys.stdin.readline()) # s: 획득 가능한 점수
    res = 0
    for j in arr:
        for k in dict[j]:
            if s-k in dict[j]:# s-k가 있으면 s 점수 획득 가능
                if k == s-k: # 같은 원기둥끼리 이어붙이는 것을 방지
                    continue
                res += 1 # 결과 누적
    print(res//2)