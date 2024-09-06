from collections import deque
def bfs(x, y,team):
    cnt = 0
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        cnt += 1
        # 상, 하, 좌, 우 탐색하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]  
            if(0 <= nx < m and 0 <= ny < n):
                if(graph[nx][ny] == team):
                    queue.append((nx, ny))
                    graph[nx][ny] = 0
    return cnt

# [설계1] 입력 받기
n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]
white = 0
blue = 0
# 상, 하, 좌, 우 탐색 방향 설정하기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(m):
    for j in range(n):
        if graph[i][j] == "W":
            white += (bfs(i,j,"W") ** 2)
        elif graph[i][j] == "B":
            blue += (bfs(i,j,"B") ** 2)

print(white,blue)