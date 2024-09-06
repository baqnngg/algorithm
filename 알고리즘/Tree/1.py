def dfs(v):
    visited[v] = 1
    for i in adj_list[v]:
        if visited[i] == 0:    
            dfs(i)

n = int(input())
DD = list(map(int,input().split()))
adj_list = [[] for _ in range(n)]
answer = [0] * (n+1)
visited = [False]*(n+1)

for i in range(n):
    adj_list[DD[i]] = adj_list[DD.index(DD[i])]
    adj_list[DD.index(DD[i])] = adj_list[DD[i]]

def DFS(s):
    visited[s] = True
    for i in adj_list[s]:
        if not visited[i]:
            answer[i] = s
            DFS(i)

DFS(1)

for i in range(2,n+1):
    print(answer[i])