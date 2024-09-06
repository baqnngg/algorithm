# [설계3] DFS(깊이우선탐색) 함수 만들기 (2) 함수 만들기
def dfs(v):
    visited[v] = 1 # 방문 리스트에 방문 처리
    for i in adj_list[v]:
        if visited[i] == 0:    
            dfs(i)

# [설계1] 입력받기(1) 노드, 간선, 탐색값 입력 받기    
n = int(input())
edge = int(input())
# [설계1] 입력받기(2) 그래프(2차원 리스트), 방문처리리스트 만들기  
adj_list = [[] for _ in range(n+1)] # graph[0][0] 사용하지 않기 위해 n+1[개] 리스트 생성(헷갈림 방지)
visited = [0]*(n+1) # visited[0] 사용하지 않기 위해 n+1[개] 리스트 생성(헷갈림 방지)

# [설계2] 인접 리스트 만들기 (1) 입력 받기
for i in range(edge):
    s, e = map(int, input().split())
    adj_list[s].append(e) 
    adj_list[e].append(s)
    
# [설계2] 인접 리스트 만들기 (2) 정렬하기
for i in range(n+1):
    adj_list[i].sort() # 번호가 작은 노드부터 방문하기 위해 각 행을 오름차순 정렬

dfs(1)
# [설계3] DFS(깊이우선탐색) 함수 만들기 (1) 함수 호출
print(sum(visited)-1)