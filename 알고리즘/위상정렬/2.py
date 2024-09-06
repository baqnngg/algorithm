from collections import deque

n,m = map(int,input().split())
adj_list = [[] for _ in range(n+1)]
ind = [0] * (n+1)

for _ in range(m):
    s,e = map(int,input().split())
    adj_list[s].append(e)
    ind[e] += 1

queue = deque()

for i in range(1,n+1):
    if ind[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    print(now,end=" ")
    for next in adj_list[now]:
        ind[next] -= 1

        if ind[next] == 0:
            queue.append(next)