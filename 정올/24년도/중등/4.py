import copy
import sys
input = sys.stdin.readline
limit_number = 15000
sys.setrecursionlimit(limit_number)

def rise(x,y):
    if x<0 or x >n-1 or y<0 or y >n-1:
        return
    if graph[x][y] <= day and graph[x][y] != 0:
        graph[x][y] = 0
        rise(x-1, y)
        rise(x, y-1)
        rise(x+1, y)
        rise(x, y+1)
        return
    return

def groups(x,y):
    global group
    if x<0 or x >n-1 or y<0 or y >n-1:
        return 
    if cpgraph[x][y] != 0:
        cpgraph[x][y] = 0
        group += 1
        groups(x-1, y)
        groups(x, y-1)
        groups(x+1, y)
        groups(x, y+1)
        return 
    return 

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
people = int(input())
day = 0

while 1:
    gg = [0]

    #물이 차오르는거 차오르면 0으로 바뀜
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= day and graph[i][j] != 0:
                rise(i,j)   

    cpgraph = copy.deepcopy(graph)
    #그룹에서 사람의 수 확인
    for i in range(n):
        for j in range(n):
            if cpgraph[i][j] == 0: continue
            else:
                group = 0
                groups(i,j)
                gg.append(group)

    if max(gg) < people:
        print(day-1)
        break

    #날짜 계산
    day += 1