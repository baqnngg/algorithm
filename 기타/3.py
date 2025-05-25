from collections import deque

def aaa(x,y):
    global cnt
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < m and 0 <= next_y < n:
                # 호수면ㄱ
                if graph[next_x][next_y] == "L":
                    graph[next_x][next_y] = "."
                    #queue에 좌표넣기
                    queue.append((next_x, next_y))

n, m = map(int, input().split())  #크기
graph = [list(input().split()) for _ in range(m)]
cnt = 0

dx, dy = [0,0,-1,1,1,1,-1,-1], [1,-1,0,0,1,-1,1,-1]  #8방향 탐색을 위한 좌표 계산에 사용됩니다

queue = deque()  #큐생성

for i in range(m):
    for j in range(n):
        if graph[i][j] == "L":
            aaa(i,j)
            cnt+=1

print(cnt)