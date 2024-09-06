from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def bfs(x, y):
    global ans
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i] 
            if ma[nx][ny] == 1 or queue.count(ma[cx][cy]) >= 1:
                ans = "YES"
                queue = deque()
                break
            if(0 <= nx < n and 0 <= ny < n):
                if(ma[nx][ny] == 0):
                    queue.append((nx, ny))
                    ma[nx][ny] = 2
n = int(input())
ma = []
ans = "NO"

dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]

for i in range(n):
    ma.append([])
    for j in range(n):
        ma[i].append(0)

ax,ay = map(int,input().split())
bx,by = map(int,input().split())
cx,cy = map(int,input().split())
ma[ax][ay] = 3
ma[cx][cy] = 1

# 적토마 위치
for i in range(n):
    ma[ax][i] = 3
for i in range(n):
    ma[i][ay] = 3
for i in range(n-ax):
    ma[i][i] = 3
for i in range(n-ax+1,n):
    ma[i][i] = 3
for i in range(1,n-ay):
    ma[i][n-i] = 3
for i in range(n-ay+1,n):
    ma[i][n-i] = 3
bfs(bx,by)
print(ans)