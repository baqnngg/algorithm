from collections import deque
import sys
#import copy
input = sys.stdin.readline

n = int(input())
adj__list = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
time = [0] * (n+1)
###
ans = [0] * (n+1)

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
        ###
        ans[i] = time[i]
#timecost = copy.deepcopy(time)

while queue:
    now = queue.popleft()
    #print(time[now])
    for next in adj__list[now]:
        indegree[next] -= 1
        #time[next] = max(time[next], time[now] + timecost[next])
        ###
        ans[next] = max(ans[next], time[next] + ans[now])
        if indegree[next] == 0:
            queue.append(next)

###
print(*ans[1:],sep='\n')