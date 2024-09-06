import copy
import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

def dfs2(color, x, y): #일반
    if x<0 or x >n-1 or y<0 or y >n-1: # 그래프 범위를 벗어나면 탐색 종료
        return False
    if cpgraph[x][y] == color: # 해당 위치가 얼음이라면
        cpgraph[x][y] = 0 # 해당 위치 방문처리
        # 상,하,좌,우 dfs 탐색하기
        dfs2(color,x-1, y)
        dfs2(color,x, y-1)
        dfs2(color,x+1, y)
        dfs2(color,x, y+1)
        return True # 얼음 덩어리가 발견되었으므로 True를 반환
    return False # 해당 위치가 얼음이 아니라면 탐색 종료

# [설계2] DFS 설계하기 (2) DFS 함수 만들기
def dfs(color, x, y): #일반
    if x<0 or x >n-1 or y<0 or y >n-1: # 그래프 범위를 벗어나면 탐색 종료
        return False
    if graph[x][y] == color: # 해당 위치가 얼음이라면
        graph[x][y] = 0 # 해당 위치 방문처리
        # 상,하,좌,우 dfs 탐색하기
        dfs(color,x-1, y)
        dfs(color,x, y-1)
        dfs(color,x+1, y)
        dfs(color,x, y+1)
        return True # 얼음 덩어리가 발견되었으므로 True를 반환
    return False # 해당 위치가 얼음이 아니라면 탐색 종료

# [설계1] 그래프 입력 받기
n = int(input())
gpcolor = 0 # 얼음 개수 
cbcolor = 0 #색맹이 보는 색깔 

graph = []
for i in range(n):
        graph.append(list(input()))
cpgraph = copy.deepcopy(graph)  #카피
# [설계2] DFS 설계하기 (1) 함수 호출
for i in range(n):
        for j in range(n):
          color = graph[i][j]
          if color == 0:
              continue
          else:
            result = dfs(color,i, j) # 해당 위치 얼음 dfs 탐색 시작
            if result == True: # 얼음이 탐색되었다면 얼음 개수 세기
                gpcolor+=1

for i in range(n):
     for j in range(n):
          color = cpgraph[i][j]
          if color == "G":
               cpgraph[i][j] = "R"

for i in range(n):
        for j in range(n):
          color = cpgraph[i][j]
          if color == 0:
               continue
          result2 = dfs2(color,i, j) # 해당 위치 얼음 탐색 시작
          if result2 == True: # 얼음이 탐색되었다면 얼음 개수 세기
              cbcolor+=1
    
print(gpcolor,cbcolor) # 정답 출력