import heapq
import sys
input = sys.stdin.readline

V = int(input())
E = int(input())
adj_list = [[] for _ in range(V+1)]
distance = [sys.maxsize] * (V+1)
visited = [False] * (V+1)

for _ in range(E):
    u,v,w = map(int,input().split())
    adj_list[u].append((v,w))

K,la = map(int,input().split())

heap = [(0,K)]
distance[K] = 0
while heap:
    now = heapq.heappop(heap)
    now_v = now[1]
    if visited[now_v] == True:
        continue
    visited[now_v] = True
    for tmp in adj_list[now_v]:
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[now_v] + value:
            distance[next] = distance[now_v] + value
            heapq.heappush(heap,(distance[next],next))

print(distance[la])