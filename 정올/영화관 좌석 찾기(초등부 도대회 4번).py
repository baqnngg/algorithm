import sys
input = sys.stdin.readline

# [설계2] DFS 설계하기 (2) DFS 함수 만들기
def dfs(x):
    global dn
    if x<0 or x >9:
        return dn
    if ll[x] == 0:
        #몇 명이 앉는지 
        dn+=1
        ll[x] = 2
        dfs(x-1)
        dfs(x+1)
        return dn
    return dn

#사람수
cn = int(input())
graph = [list(map(int,input().split())) for _ in range(10)]
cc = []
dn = 0

for i in range(10):
    for j in range(10):
        if graph[i][j] == 0:
            ll = graph[i]
            a = dfs(j)
            if a >= cn:
                cc.append(i+1)
            dn = 0

if cc == []:
    print(-1)
else:
    cc.sort(reverse=True)
    print(cc[0])