from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        # 상, 하, 좌, 우 탐색하기
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            
            # 탐색을 무시해도 되는 경우 설계하기
            # 무시(1) 미로 범위를 벗어난 경우 무시하기
            if next_x < 0 or next_x >=n or next_y < 0 or next_y >= m:
                continue
            # 무시(2) 벽인 경우 무시하기
            if graph[next_x][next_y] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우, 최단 거리 기록(방문처리) 후 큐에 삽입하여 다음 탐색 실행
            if graph[next_x][next_y] == 1:
                if next_x == 0 and next_y == 0:
                    continue
                graph[next_x][next_y] = graph[x][y] + 1 # 최단 거리 기록(방문처리)
                queue.append((next_x, next_y))

# [설계1] 입력 받기
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우 탐색 방향 설정하기
dx = [-1, 1, 0, 0] # 예를 들어 (dx, dy)가 (-1, 0)인 경우 '상' 방향을 의미
dy = [0, 0, -1, 1]

# bfs 함수 호출
bfs(0, 0) # 탐색 시작 위치는 (0,0)
# 정답 출력
print(graph[n-1][m-1]) # 도착지의 거리값을 출력