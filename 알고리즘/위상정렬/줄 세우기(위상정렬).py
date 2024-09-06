from collections import deque

n,m = map(int,input().split())
adj__list = [[] for _ in range(n+1)]

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
    now = queue.popleft()
    print(now,end=" ")
    for next in adj__list[now]:
        indegree[next] -= 1

        if indegree[next] == 0:
            queue.append(next)