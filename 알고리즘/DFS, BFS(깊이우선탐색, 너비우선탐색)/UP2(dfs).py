# [설계2] DFS 설계하기 (2) DFS 함수 만들기
def dfs(x, y, pp):
    global cnt
    if x<0 or x >n-1 or y<0 or y >m-1: # 그래프 범위를 벗어나면 탐색 종료
        return False
    if graph[x][y] == pp: # 해당 위치가 얼음이라면
        graph[x][y] = -1 # 해당 위치 방문처리
        cnt += 1
        # 상,하,좌,우 dfs 탐색하기
        dfs(x-1, y, pp)
        dfs(x, y-1,pp)
        dfs(x+1, y,pp)
        dfs(x, y+1,pp)
        return True # 얼음 덩어리가 발견되었으므로 True를 반환
    
    return False # 해당 위치가 얼음이 아니라면 탐색 종료
# [설계1] 그래프 입력 받기
n, m = map(int, input().split()) 
cnt = 0
cc = [0]
graph = []
gg = []
for i in range(n):
        graph.append(list(map(int, input().split())))
for j in range(n):
    gg.append(max(graph[j]))
maxnum = max(gg)
# [설계2] DFS 설계하기 (1) 함수 호출
for x in range(maxnum+1):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == x:
                result = dfs(i, j, x) # 해당 위치 얼음 dfs 탐색 시작
                cc.append(cnt)
                cnt = 0
    if cc == [0]:
        continue
    mm = max(cc)
    cc = [0]
    print(x,mm)