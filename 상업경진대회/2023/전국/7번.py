from collections import deque
import sys

def BB(x,y):
    global ma
    queue = deque()
    queue.append([x,y,ma[0][0]])
    ma[0][0] = '0'

    while queue:
        qq,pp = [],[]
        x, y, m = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == n - 1 and ny == n - 1:
                return m+ma[nx][ny]
            if(0 <= nx < n and 0 <= ny < n and ma[nx][ny] != '0'):
                qq.append([nx,ny])
                pp.append(ma[nx][ny])
                ma[nx][ny] = "0"
        queue.append([qq[pp.index(min(pp))][0],qq[pp.index(min(pp))][1],m+min(pp)])

n = int(input())
ma = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [1,-1,0,0],[0,0,1,-1]
print(BB(0,0))