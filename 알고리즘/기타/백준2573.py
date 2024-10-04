import sys
import copy

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(x, y):
    if x<0 or x >m-1 or y<0 or y >n-1:
        return
    if icebergcp[x][y] != 0:
        icebergcp[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return
    
    return

m, n = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(m)]
year = 0

while 1:
    # 여기에서 빙산이 몇개 있는지 판단
    icebergcp = copy.deepcopy(iceberg)
    cnt = 0
    for i in range(m):
        for j in range(n):
            if icebergcp[i][j] != 0:
                dfs(i, j)
                cnt += 1
        if icebergcp.count(0) == m*n:
            break

    if cnt >= 2:
        print(year)
        break
    if cnt == 0:
        print(0)
        break

    # 여기에서 동서남북에 있는 바다의 개수를 빼줌
    icebergcp = copy.deepcopy(iceberg)
    for i in range(m):
        for j in range(n):
            if icebergcp[i][j] != 0:
                if icebergcp[i - 1][j] == 0:
                    iceberg[i][j] -= 1
                if icebergcp[i][j - 1] == 0:
                    iceberg[i][j] -= 1
                    if iceberg[i][j] < 0:
                        iceberg[i][j] = 0
                if icebergcp[i + 1][j] == 0:
                    iceberg[i][j] -= 1
                    if iceberg[i][j] < 0:
                        iceberg[i][j] = 0
                if icebergcp[i][j + 1] == 0:
                    iceberg[i][j] -= 1
                    if iceberg[i][j] < 0:
                        iceberg[i][j] = 0.
    year += 1

