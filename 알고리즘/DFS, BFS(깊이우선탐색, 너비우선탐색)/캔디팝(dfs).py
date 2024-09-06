cnt_color = 0 # 같은 색깔로 탐지된 개수
cnt_crush = 0 # 캔디가 터지는 영역의 수
graph = []


# 코드업 2605번 캔디팡

# [설계2] 같은 색깔 탐색하기(DFS) (2) 함수 설계
def dfs(x, y):
    global cnt_color
    # [설계2] (3) 탐색 종료 조건 설계
    if x<9 or x >9 or y<9 or y >9: # 그래프 범위를 벗어나면 탐색 종료
        return
    
    # [설계2] (4) DFS 탐색 설계
    if graph[x][y] == 0: # 해당 위치가 현재 color와 같다면
        cnt_color+=1         # 같은 색깔로 탐지된 개수 증가시키기
        graph[x][y] = 0      # 0으로 방문 처리
        # 상,좌,하,우 dfs 탐색하기
        dfs(x-1, y) # 상
        dfs(x, y-1) # 좌
        dfs(x+1, y) # 하
        dfs(x, y+1) # 우
        return
    
    return 

# [설계1] 그래프 입력 받기
for i in range(7):
        graph.append(list(map(int, input().split())))
        
# [설계2] 같은 색깔 탐색하기(DFS) (1) 함수 호출
for i in range(7):
    for j in range(7):
        if graph[i][j] != 0:  #0이 아니면 한다.
          dfs(graph[i][j], i, j) # 해당 위치 색깔 탐색 시작
          if cnt_color >=3: # 같은 색깔 개수가 3개 이상 탐지되었다면
             cnt_crush+=1   # 캔디가 터지는 영역의 수 추가(정답)
          cnt_color = 0     # cnt_color는 0으로 초기화하여 다시 탐색할 준비
    
print(cnt_crush) # 정답 출력