# from collections import deque
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**5)

# def popo():
#     global cnt
#     queue = deque()
#     queue.append((0,0,[[0,0]]))
#     while queue:
#         x, y, move = queue.popleft()
#         for i in range(4):
#             nx,ny = x+dy[i], y+dx[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m or (move in [nx,ny]):
#                 continue
#             if nx == n-1 and ny == m-1:
#                 cnt += 1
#                 continue
#             if (graph[x][y] > graph[nx][ny]):
#                 queue.append((nx,ny,move+[[nx,ny]]))
#     return cnt

# n,m = map(int,input().split())
# graph = [list(map(int,input().split())) for _ in range(n)]
# cnt = 0
# dx,dy = [1,-1,0,0],[0,0,1,-1]
# print(popo())


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0  # 초기화
    
    for d in range(4):
        nx, ny = x + dy[d], y + dx[d]
        if 0 <= nx < M and 0 <= ny < N and graph[x][y] > graph[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dp[M-1][N-1] = 1  # 도착점은 1로 초기화

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]  # 이동 방향 (하, 상, 우, 좌)

# 시작점 (0, 0)에서 도착점 (M-1, N-1)까지의 경로 개수 계산
print(dfs(0, 0))
