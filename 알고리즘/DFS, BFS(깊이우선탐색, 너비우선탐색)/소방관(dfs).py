import copy # 깊은 복사를 위함.
flag = 0 #0이면 불 X, 1이면 불 O
# [설계3] 옮겨 붙는 불 주위를 소방관으로 바꾸기 (2) 함수 설계
def change():
    for i in range(10):
        for j in range(10):
            if(temp_graph[i][j] == 3): # 해당 위치가 옮겨 붙는 불이라면
                # 상, 하, 좌, 우를 소방관(9)으로 바꾸기
                if(i-1 >= 0):
                    if(temp_graph[i-1][j] == 0):
                        graph[i-1][j] = 9
                if(i+1 <=9):
                    if(temp_graph[i+1][j] == 0):
                        graph[i+1][j] = 9
                if(j-1>=0):
                    if(temp_graph[i][j-1]==0):
                        graph[i][j-1] = 9
                if(j+1 <= 9):                    
                    if(temp_graph[i][j+1] == 0):
                        graph[i][j+1] = 9
 # [설계4] 정답 출력(2) 함수 설계                   
def print_map():
    for i in range(10):
        for j in range(10):
            print(graph[i][j], end=" ")
        print()
                                                    
# [설계2] 옮겨 붙는 불 계산하기(DFS)(2) 함수 설계
def dfs(x, y):
    global flag
    # [설계2] (3) DFS 종료 조건 설계
    if x<0 or x >9 or y<0 or y >9: # 그래프 범위를 벗어나면 탐색 종료
        return False
    
    # [설계2] (4) 불이 난 상황 표시하기
    if temp_graph[x][y] == 1:
        flag = 1

    # [설계2] (5) 옮겨 붙는 불 계산하기 -> 해당 위치를 3으로 바꿈.
    if temp_graph[x][y] == 1 or temp_graph[x][y] == 2 and flag == 1: # 해당 위치가 불 또는 나무라면
            temp_graph[x][y] = 3 # 해당 위치 불처리
            # 상,좌,하,우 dfs 탐색하기
            dfs(x-1, y) # 상
            dfs(x, y-1) # 좌
            dfs(x+1, y) # 하
            dfs(x, y+1) # 우
            return  
    return 

# [설계1] 10*10 map 입력 받기
graph = []
for i in range(10):
    graph.append(list(map(int, input().split())))
# 옮겨붙는 불 계산을 위한 리스트의 깊은 복사
temp_graph = copy.deepcopy(graph)

# [설계2] 옮겨 붙는 불 계산하기(DFS)(1) 함수 호출
for i in range(10):
    for j in range(10):
          dfs(i, j) # 해당 위치에서 옮겨 붙는 불 계산 시작
          flag = 0  # flag를 0으로 초기화(0이면 불이 안남. 1이면 불이 난 상황)
# [설계3] 옮겨 붙는 불 주위를 소방관으로 바꾸기 (1) 함수 호출
change()    
# [설계4] 정답 출력 (1) 함수 호출
print_map()