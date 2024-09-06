from collections import deque #큐를 쓰기위해 임포트

def virus_spread():
    global max

    while queue:
        cycle, x, y = queue.popleft()
        if max < cycle:
            max = cycle

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                continue
            if graph[next_x][next_y] == 1:
                graph[next_x][next_y] = -1
                queue.append((cycle +1 , next_x, next_y))

n, m = map(int, input().split())  #크기
max = -1
graph = []
virus_data = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  #4방향 탐색을 위한 좌표 계산에 사용됩니다


#1,2,3의 좌표받기
for i in range(n):
    for j in range(m):
        if graph[i][j] == -1:
            virus_data.append((0, i, j))
queue = deque(virus_data)  #큐생성

virus_spread()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            print(0)
            exit()

print(max)