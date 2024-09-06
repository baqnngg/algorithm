from collections import deque
import sys
import copy
input = sys.stdin.readline

n = int(input())
adj__list = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
time = [0] * (n+1)

for i in range(1,n+1):
    f = list(map(int,input().split()))[:-1]
    time[i] = f[0]
    build = f[1:]
    for j in build:
        adj__list[j].append(i)
        indegree[i] += 1

queue = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)

timecost = copy.deepcopy(time)
while queue:
    now = queue.popleft()
    #바로 찍으면 안되네
    #print(time[now])
    for next in adj__list[now]:
        indegree[next] -= 1
        #max함수를 쓰는 것은 알고있었지만 어떻게 쓰는지 모름
        time[next] = max(time[next], time[now] + timecost[next])
        if indegree[next] == 0:
            queue.append(next)

#출력방식이 달라서 틀릴수 있구나
print(*time[1:],sep='\n')