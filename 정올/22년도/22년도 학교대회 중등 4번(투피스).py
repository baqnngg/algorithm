from collections import deque
import sys
input = sys.stdin.readline

def bfs(search_start):
    global cnt
    queue = deque() 
    queue.append(search_start)
    visited[search_start] = 1
    if treasure.count(search_start) > 0:
        cnt += 1

    while queue:
        now_node = queue.popleft() 
        for next_node in adj_list[now_node]: 
            if visited[next_node] != 1:
                if treasure.count(next_node) > 0:
                    cnt += 1
                visited[next_node] = 1 
                queue.append(next_node)

n, m, t, start = map(int, input().split()) 
adj_list = [[] for _ in range(n + 1)]
visited = [0]*(n+1)
cnt = 0
treasure = list(map(int,input().split()))

# 인접 리스트 만들기
for _ in range(m):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

bfs(start)
print(cnt)