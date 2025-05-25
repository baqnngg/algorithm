from collections import deque
import copy

#옮겨 붙은 불 계산
def aaa(x,y):
    global cnt
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < 10 and 0 <= next_y < 10:
                # 불 근처에 나무가 있으면 불로 바꿈
                if graphcp[next_x][next_y] == 2:
                    graphcp[next_x][next_y] = 1
                    queue.append((next_x, next_y))
                    fire.append((next_x, next_y))

graph1 = [list(map(int,input().split())) for _ in range(10)]
cnt = 0

dx, dy = [0,0,-1,1], [1,-1,0,0]  #8방향 탐색을 위한 좌표 계산에 사용됩니다

queue = deque()  #큐생성

#불의 위치 저장
fire = []

# 옮겨 붙은 불 계산
graphcp = copy.deepcopy(graph1)
for i in range(10):
    for j in range(10):
        if graph1[i][j] == 1:
            aaa(i,j)
            fire.append((i,j))

for i in fire:
    x,y = i
    for j in range(4):
        next_x, next_y = x + dx[j], y + dy[j]
        if 0 <= next_x < 10 and 0 <= next_y < 10:
            if graphcp[next_x][next_y] == 0:
                graph1[next_x][next_y] = 9

for i in range(10):
    print(*graph1[i])