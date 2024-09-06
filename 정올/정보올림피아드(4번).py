from collections import deque

#처음 min_ch...에서 안막히려고
min_change = 99999
def channel_change():
    global min_change, cnt
    vis = [False] * m
    while queue:
        o = queue.popleft()
        if o[1] > min_change:
            break

        if o[0] == 0:
            min_change = o[1]

        for i in range(len(um)):
            queue.append([(o[0]*um[i][0]+um[i][1])%m,o[1]+1])
    min_change = -1
m,n,s = map(int,input().split())
um = [list(map(int,input().split())) for _ in range(n)]
# start, target =  map(int, input().split())
queue = deque()
queue.append([s,0])
channel_change()

print(min_change)