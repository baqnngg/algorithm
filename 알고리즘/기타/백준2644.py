import heapq
import sys
input = sys.stdin.readline

n = int(input())
a,b = map(int,input().split())
m = int(input())

def tree(v):
    q=[]
    heapq.heappush(q, (0, v))
    distance[v]=0
    while q:
        dist, now= heapq.heappop(q)
        for i in adj_list[now]:
            if distance[i] != 0:
                continue
            cost = dist + 1
            distance[i]=cost
            heapq.heappush(q, (cost, i))

adj_list = [[] for _ in range(n+1)]
distance = [0] *(n+1)

for _ in range(m):
    s,e = map(int,input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

tree(a)

if distance[b] == 0:
    print(-1)
else:
    print(distance[b])