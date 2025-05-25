from collections import deque

n = int(input())
h = list(map(int, input().split()))
queue = deque()
queue.append(h.index(max(h)))
cnt = 0

while queue:
    x = queue.popleft()
    if x - 1 >= 0:
        if h[x-1] <= h[x]:
            queue.append(x-1)
    if x + 1 < n:
        if h[x+1] <= h[x]:
            queue.append(x+1)
    cnt += 1

print(cnt)