from collections import deque
import copy
def ec():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                continue
            if graph[next_x][next_y] == "0":
                graph[next_x][next_y] = "1"
                queue.append((next_x, next_y))

m, n = map(int,input().split())
queue = deque()
graph = [list(input()) for _ in range(m)]
copygraph = copy.deepcopy(graph)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(n):
    if graph[0][i] == "0":
        queue.append((0,i))
        ec()
if graph[m-1] == copygraph[m-1]:
    print("NO")
else:
    print("YES")