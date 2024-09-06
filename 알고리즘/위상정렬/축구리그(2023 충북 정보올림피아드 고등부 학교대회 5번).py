#위상정렬
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
adj__list = [[] for _ in range(n+1)]
pp = 0
indegree = [0] * (n+1)

for i in range(m):
    s,e = map(int,input().split())
    adj__list[s].append(e)
    indegree[e] += 1

queue = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    #유일X
    if len(queue) >= 2:
        pp = 1
    now = queue.popleft()
    for next in adj__list[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

for i in range(1,n+1):
    if indegree[i] != 0:
        pp = -1
        break
print(pp)