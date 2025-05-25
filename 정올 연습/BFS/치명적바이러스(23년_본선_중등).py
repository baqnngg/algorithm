from collections import deque

def bfs():
    global max
    queue = deque(virus)
    
    while queue:
        x,y, cycle = queue.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m and graph[next_x][next_y] == 1:
                graph[next_x][next_y] = -1
                queue.append((next_x, next_y, cycle + 1))
    max = cycle

n,m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
max = 0

virus = deque()
dx,dy = [0,0,-1,1], [-1,1,0,0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == -1: # 바이러스 위치 저장
            virus.append((i,j,0))

bfs()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1: # 일반인이 있으면
            print(0)
            exit()

print(max)