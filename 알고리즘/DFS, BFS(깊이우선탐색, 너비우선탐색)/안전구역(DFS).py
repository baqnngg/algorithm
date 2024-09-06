import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x,y):
    if x<0 or x >n-1 or y<0 or y >n-1:
        return False
    if graphcp[x][y] != 0: 
        graphcp[x][y] = 0 
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True 
    return False 

n = int(input())
cnt = 0
cntt = []
graph = [list(map(int,input().split())) for _ in range(n)]

mingraph = min(graph[0])
maxgraph = max(graph[0])
for i in range(1,n):
    mingraph = min(mingraph,min(graph[i]))
for i in range(1,n):
    maxgraph = max(maxgraph,max(graph[i]))

# 만약 maxgraph 와 mingraph가 같을 때 1로 안되고 그냥 0이 출력되는 문제해결
if maxgraph == mingraph:
    cntt.append(maxgraph)

# mingraph에서 1씩 올라가면서 영역을 구할거기 때문에 for문씀
for k in range(maxgraph):

    # 가장 작은값부터 차례차례 방문처리하며 저장
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= mingraph:
                graph[i][j] = 0
    
    # 카피해서 여기에서 DFS로 영역구하기
    graphcp = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if graphcp[i][j] > mingraph:
                dfs(i,j)
                cnt += 1
    
    # 영역구한값 저장
    cntt.append(cnt)
    # 만약 cnt가 0인 경우는 이미 다 침수된 상태이기 때문에 break 
    if cnt == 0:
        break
    # 초기화
    cnt = 0
    # 여기서 가장작은값이 늘어나는 부분(1씩 더하기)
    mingraph += 1

#구한 값 출력
print(max(cntt))