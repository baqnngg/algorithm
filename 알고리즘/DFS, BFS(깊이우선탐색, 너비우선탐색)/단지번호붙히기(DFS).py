import sys
sys.setrecursionlimit(10000)

# [설계2] DFS 설계하기 (2) DFS 함수 만들기
def dfs(x, y):
    global dn
    if x<0 or x >n-1 or y<0 or y >n-1: # 그래프 범위를 벗어나면 탐색 종료
        return False
    if graph[x][y] == 1: # 단지면 ㄱ
        dn+=1
        graph[x][y] = 0 # 해당 위치 방문처리
        # 상,하,좌,우 dfs 탐색하기
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True # 단지면 true
    
    return False # 단지가 아니라면 탐색 종료
# [설계1] 그래프 입력 받기
n = int(input())
cnt_ice = 0 # 단지 개수 
dn = 0
cn = []
graph = []
for i in range(n):
        graph.append(list(map(int, input())))
# [설계2] DFS 설계하기 (1) 함수 호출
for i in range(n):
    for j in range(n):
          result = dfs(i, j) # 해당 위치 단지 dfs 탐색 시작
          if dn > 0:
               cn.append(dn)
               dn = 0
          if result == True: # 단지 개수 새기
              cnt_ice+=1

cn.sort()
print(cnt_ice) # 정답 출력
for i in range(cnt_ice):
    print(cn[i])