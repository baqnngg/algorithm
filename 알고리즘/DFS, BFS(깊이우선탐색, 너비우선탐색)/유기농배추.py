import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

def dfs(x, y):
    if x<0 or x >M-1 or y<0 or y >N-1: 
        return False
    if MNgraph[x][y] == 1:
        MNgraph[x][y] = 0

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    return False

cnt = 0
T = int(input())
for i in range(T):
    MNgraph = []
    M, N, K  = map(int, input().split())
    for i in range(M):
        MNgraph.append([])
        for j in range(N):
            MNgraph[i].append(0)

    for i in range(K):
        c,u = map(int,input().split())
        MNgraph[c][u] = 1

    for i in range(M):
        for j in range(N):
          result = dfs(i, j)
          if result == True: 
              cnt += 1      
              
    print(cnt) 
    cnt = 0