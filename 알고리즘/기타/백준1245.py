import sys
from collections import deque
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def dfs(x, y):
    global ss,an, cc
    if x<0 or x >n-1 or y<0 or y >m-1:
        return False
    if [x,y] in cc:
        an = False
        return
    for i in range(8):
        if ([x+dx[i],y+dy[i]] in ss) or (0>x+dx[i] or n-1<x+dx[i] or 0>y+dy[i] or m-1<y+dy[i]):
            continue
        if graph[x][y] < graph[x+dx[i]][y+dy[i]]:
            an = False
            return
        elif graph[x][y] == graph[x+dx[i]][y+dy[i]]:
            ss.append([x+dx[i],y+dy[i]])
            dfs(x+dx[i],y+dy[i])
            if not an:
                return
    return an


n, m = map(int, input().split())
cnt = 0
graph = []
dx,dy = [1, -1, 0, 0, 1, 1, -1, -1],[0, 0, 1, -1, 1, -1, 1, -1]
cc = []
for i in range(n):
    graph.append(list(map(int, input().split())))
kk = copy.deepcopy(graph)
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            kk[i][j] = 0
            ss = []
            an = True
            result = dfs(i, j)
            if result:
                cc.append([i,j])
                cnt+=1
print(cnt)