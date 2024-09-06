import sys
input = sys.stdin.readline
testcnt = int(input())
for _ in range(testcnt):
    n,m = map(int,input().split())
    graph = [list(input()) for _ in range(n)]
    xmin = [], ymin = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'D':
                xmin.append(i)
                ymin.append(j)
    xmin = min(xmin)
    ymin = min(ymin)
    if graph[xmin][ymin] == "D":
        print("O")
    else:
        print("X")