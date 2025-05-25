# 뭉치면 살고 흩어지면 죽는다!
import copy
import sys
input = sys.stdin.readline
limit_number = 15000
sys.setrecursionlimit(limit_number)

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

    for i in range(n):
        for j in range(n):
            if graph[i][j] <= day and graph[i][j] != 0:
                graph[i][j] = 0

    cpgraph = copy.deepcopy(graph)
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

    day += 1