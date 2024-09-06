# [설계2] DFS 설계하기 (2) DFS 함수 만들기
def dfs(x, y):
    if x<0 or x >n-1 or y<0 or y >m-1: # 그래프 범위를 벗어나면 탐색 종료
        return False
    if graph[x][y] == 0: # 해당 위치가 얼음이라면
        graph[x][y] = 1 # 해당 위치 방문처리
        # 상,하,좌,우 dfs 탐색하기
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True # 얼음 덩어리가 발견되었으므로 True를 반환
    
    return False # 해당 위치가 얼음이 아니라면 탐색 종료
# [설계1] 그래프 입력 받기
n, m = map(int, input().split())
cnt_ice = 0 # 얼음 개수 

graph = []
for i in range(n):
        graph.append(list(map(int, input())))
# [설계2] DFS 설계하기 (1) 함수 호출
for i in range(n):
    for j in range(m):
          result = dfs(i, j) # 해당 위치 얼음 dfs 탐색 시작
          if result == True: # 얼음이 탐색되었다면 얼음 개수 세기
              cnt_ice+=1
    
print(cnt_ice) # 정답 출력