from collections import deque #큐를 쓰기위해 임포트

m, n = map(int, input().split())  #토마토상자 크기
box = [list(map(int, input().split())) for _ in range(n)] #토마토 상태 입력받기 ###리스트안에 리스트를 인풋받음
queue = deque([])  #큐생성
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  #4방향 탐색을 위한 좌표 계산에 사용
res = 0

#토마토의 위치 탐색
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft() #왼쪽에 있는 큐부터 
        for i in range(4): #4방향 탐색을 위해 4번 탐색
            nx, ny = dx[i] + x, dy[i] + y  #4방향탐색
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0: #만약에 탐색범위 안에 있고 동시에 0이라면 실행
                box[nx][ny] = box[x][y] + 1                   #그 좌표에 이전좌표에 있던 숫자에 1을 더해서 넣는다
                queue.append([nx, ny])                              #큐에 좌표 넣음

bfs()
for i in box: #for문 2개 쓰는이유 : 상자를 다탐색할려고
    for j in i:  
        if j == 0:#0이 있으면 다못채운거기 때문에 
            print(-1) #print(-1)함
            exit(0)   #프로그램 종료
    res = max(res, max(i)) #res에 저장된값과 i에 저장된 값중에 큰거 저장

print(res - 1) #-1 해주는 이유 : 첫 번째 시작할때 1로 시작해서 마지막 숫자가 1더 늘어나있기 때문