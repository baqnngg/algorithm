import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
cnt_crush = 0 # 캔디가 터지는 영역의 수
graph = []
# 코드업 2605번 캔디팡

# [설계2] 같은 색깔 탐색하기(DFS) (2) 함수 설계
def dfs(x, y):
    # [설계2] (3) 탐색 종료 조건 설계
    if x < 0 or x > a-1 or y < 0 or y > b-1: # 그래프 범위를 벗어나면 탐색 종료
        return
    
    # [설계2] (4) DFS 탐색 설계
    if graph[x][y] == "L": # 해당 위치가 현재 color와 같다면
        graph[x][y] = "."      # 0으로 방문 처리
        # 상,좌,하,우 dfs 탐색하기
        dfs(x-1, y) # 상
        dfs(x, y-1) # 좌
        dfs(x+1, y) # 하
        dfs(x, y+1) # 우
        dfs(x-1, y-1) # 왼쪽위
        dfs(x-1, y+1) # 오른쪽위
        dfs(x+1, y-1) # 왼쪽아래
        dfs(x+1, y+1) # 오른쪽아래
        return
    
    return

a,b = map(int,input().split())
# [설계1] 그래프 입력 받기
for i in range(b):
        graph.append(list(input().split()))
        
# [설계2] 같은 색깔 탐색하기(DFS) (1) 함수 호출
for i in range(a):
    for j in range(b):
        if graph[i][j] != ".":
            dfs(i, j) # 해당 위치 색깔 탐색 시작
            cnt_crush+=1   # 캔디가 터지는 영역의 수 추가(정답)
    
print(cnt_crush) # 정답 출력