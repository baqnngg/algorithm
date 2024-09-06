import copy
# [설계2] DFS 설계하기 (2) DFS 함수 만들기
def dfs(x, y):
    if x<0 or x >n-1 or y<0 or y >m-1: # 그래프 범위를 벗어나면 탐색 종료
        return False
    if graph[x][y] == 1: # 해당 위치가 얼음이라면
        graph[x][y] = 0 # 해당 위치 방문처리
        # 상,하,좌,우 dfs 탐색하기
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True # 얼음 덩어리가 발견되었으므로 True를 반환
    
    return False # 해당 위치가 얼음이 아니라면 탐색 종료

def dfs2(x, y):
    if x<0 or x >n-1 or y<0 or y >m-1: # 그래프 범위를 벗어나면 탐색 종료
        return False
    if graph2[x][y] == 0: # 해당 위치가 얼음이라면
        graph2[x][y] = 1 # 해당 위치 방문처리
        # 상,하,좌,우 dfs 탐색하기
        dfs2(x-1, y)
        dfs2(x, y-1)
        dfs2(x+1, y)
        dfs2(x, y+1)
        return True # 얼음 덩어리가 발견되었으므로 True를 반환
    
    return False # 해당 위치가 얼음이 아니라면 탐색 종료

# [설계1] 그래프 입력 받기
n, m = map(int, input().split())
cnt_ice = 0 # 얼음 개수 
cnt_ice2 = 0 # 얼음 개수 
graph = []
for i in range(n):
        graph.append(list(map(int, input().split())))
graph2 = copy.deepcopy(graph)
# [설계2] DFS 설계하기 (1) 함수 호출
for i in range(n):
    for j in range(m):
            if graph[i][j] == 1:
                result = dfs(i, j) # 해당 위치 얼음 dfs 탐색 시작
                if result == True:
                    cnt_ice2 += 1

for i in range(n):
    for j in range(m):
            if graph2[i][j] == 0:
                result = dfs2(i, j) # 해당 위치 얼음 dfs 탐색 시작
                if result == True:
                    cnt_ice += 1
    
print(cnt_ice,cnt_ice2) # 정답 출력