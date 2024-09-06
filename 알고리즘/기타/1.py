from collections import deque

def bfs(search_start):
    queue = deque() 
    queue.append(search_start)
    visited[search_start] = 1
    
    while queue:
        now_node = queue.popleft() 
        print(now_node, end=' ')
        for next_node in adj_list[now_node]: 
            if visited[next_node] != 1:
                visited[next_node] = 1 
                queue.append(next_node)

n, edge, search_start = map(int, input().split()) 
adj_list = [[] for _ in range(n+1)] 
visited = [0]*(n+1) 

for i in range(edge):
    s, e = map(int, input().split())
    adj_list[s].append(e) 
    adj_list[e].append(s)
    

for i in range(n+1):
    adj_list[i].sort()
    
bfs(search_start)