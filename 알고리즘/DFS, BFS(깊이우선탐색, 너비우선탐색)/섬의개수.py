from collections import deque
import sys
input = sys.stdin.readline

def cntis(x,y):
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(8): #8방향탐색을 위해서 8번 실행
            next_x = x + dx[i]
            next_y = y + dy[i]

            #범위를 벗어나면 continue
            if next_x < 0 or next_x >= h or next_y < 0 or next_y >= w:
                continue

            # 호수면ㄱ
            if island[next_x][next_y] == 1:
                island[next_x][next_y] = 0
                #queue에 좌표넣기
                queue.append((next_x, next_y))

w,h = 1,1
dx, dy = [0,0,-1,1,1,1,-1,-1], [1,-1,0,0,1,-1,1,-1]  #8방향 탐색을 위한 좌표 계산에 사용됩니다
cnt = [] #섬의 개수 저장목적
cntt = 0
while w != 0 and h != 0:
    w,h = map(int,input().split())
    island = [list(map(int,input().split())) for _ in range(h)]
    queue = deque()
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                cntis(i,j)
                cntt += 1
    cnt.append(cntt)
    cntt = 0
for i in range(len(cnt)-1):
    print(cnt[i])