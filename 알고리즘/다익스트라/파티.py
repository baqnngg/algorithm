import heapq
import sys
input = sys.stdin.readline

V,E,K = map(int,input().split())
adj_list = [[] for _ in range(V+1)]
distance = [sys.maxsize] * (V+1)
visted = [False] * (V+1)

for _ in range(E):
    u,v,w = map(int,input().split())
    adj_list[u].append((v,w))

heap = [(0,K)]
distance[K] = 0
while heap:
    now = heapq.heappop(heap)
    now_v = now[1]
    if visted[now_v] == True:
        continue
    visted[now_v] = True
    for tmp in adj_list[now_v]:
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[now_v] + value:
            distance[next] = distance[now_v] + value
            heapq.heappush(heap, (distance[next],next))

print(max(distance))