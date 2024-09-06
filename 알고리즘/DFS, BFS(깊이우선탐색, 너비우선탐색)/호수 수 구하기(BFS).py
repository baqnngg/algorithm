from collections import deque #큐를 쓰기위해 임포트

def aaa(x,y):
    #호수 개수 체크
    global cnt
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(8): #8방향탐색을 위해서 8번 실행
            next_x = x + dx[i]
            next_y = y + dy[i]

            #범위를 벗어나면 continue
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                continue

            # 호수면ㄱ
            if graph[next_x][next_y] == "L":
                graph[next_x][next_y] = "."
                #queue에 좌표넣기
                queue.append((next_x, next_y))

n, m = map(int, input().split())  #크기
graph = []
cnt = 0
for i in range(m):
    graph.append(list(input().split()))

dx, dy = [0,0,-1,1,1,1,-1,-1], [1,-1,0,0,1,-1,1,-1]  #8방향 탐색을 위한 좌표 계산에 사용됩니다

queue = deque()  #큐생성

for i in range(m):
    for j in range(n):
        if graph[i][j] == "L":
            aaa(i,j)
            cnt+=1

print(cnt)