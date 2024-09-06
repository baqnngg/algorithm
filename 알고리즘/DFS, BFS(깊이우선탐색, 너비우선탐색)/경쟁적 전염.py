from collections import deque #큐를 쓰기위해 임포트

def virus_spread():
    while queue:
        virus, s, x, y = queue.popleft()
        if s == target_s:
            break
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
                continue
            if graph[next_x][next_y] == 0:
                graph[next_x][next_y] = virus
                queue.append((virus, s+1, next_x,next_y))

n, k = map(int, input().split())  #크기
graph = []
virus_data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
target_s, target_x, target_y = map(int,input().split())


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  #4방향 탐색을 위한 좌표 계산에 사용됩니다


#1,2,3의 좌표받기
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus_data.append((graph[i][j], 0, i, j))
virus_data.sort() #정렬
queue = deque(virus_data)  #큐생성

virus_spread()

print(graph[target_x-1][target_y-1])