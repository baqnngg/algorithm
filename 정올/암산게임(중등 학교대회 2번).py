#내꺼
import copy
n,m = map(int,input().split())
ca = [list(map(int,input().split())) for _ in range(m)]
ca2 = []
for i in range(m):
    pp = copy.deepcopy(ca[i])
    pp = list(reversed(pp))
    ca2.append(pp)
for i in range(m):
    for j in range(n):
        ca[i][j] += ca2[i][j]
for i in range(m):
    print(*ca[i])