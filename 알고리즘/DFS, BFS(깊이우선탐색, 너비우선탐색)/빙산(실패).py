import sys
import copy
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x, y):
    if x<0 or x >n-1 or y<0 or y >m-1: # 그래프 범위를 벗어나면 탐색 종료
        return True
    if icebergcp[x][y] != 0:
        icebergcp[x][y] = 0
        # 상,하,좌,우 dfs 탐색하기
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    return True

# 입력받기
m,n = map(int,input().split())
iceberg = [list(map(int,input().split())) for _ in range(m)]
cnt = 0
year = 0
while max(iceberg) != 0:
    #빙산높이 줄이기
    icebergcp = copy.deepcopy(iceberg)
    for i in range(m):
        for j in range(n):
            if icebergcp[i][j] != 0:
                if icebergcp[i-1][j] == 0:
                    iceberg[i][j] -= 1
                if icebergcp[i][j-1] == 0:
                    iceberg[i][j] -= 1
                    if iceberg[i][j] < 0:
                        iceberg[i][j] = 0
                if icebergcp[i+1][j] == 0:
                    iceberg[i][j] -= 1
                    if iceberg[i][j] < 0:
                        iceberg[i][j] = 0
                if icebergcp[i][j+1] == 0:
                    iceberg[i][j] -= 1 
                    if iceberg[i][j] < 0:
                        iceberg[i][j] = 0
                        
    year += 1

    #빙산 몇개인지 보기
    icebergcp = copy.deepcopy(iceberg)
    for i in range(m):
        for j in range(n):
            if icebergcp[i][j] != 0:
                dfs(i,j)
                cnt += 1

    if cnt >= 2:
        print(year)
        break

    if cnt == 0:
        print(0)
        break