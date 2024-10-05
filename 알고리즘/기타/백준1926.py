import  sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def ss(x,y):
    global cc
    if 0>x or x>n-1 or 0>y or y>m-1:
        return
    if graph[x][y] == 1:
        graph[x][y] = 0
        cc += 1
        ss(x-1,y)
        ss(x,y-1)
        ss(x+1,y)
        ss(x,y+1)
        return
    return

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cnt = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cc = 0
            ss(i,j)
            cnt.append(cc)

if len(cnt) == 0:
    print(len(cnt))
    print(0)
else:
    print(len(cnt))
    print(max(cnt))