from collections import deque

#처음 min_ch...에서 안막히려고
min_change = 99999
#최소 버튼 조작 횟수로 이동하는 방법의 가짓수
cnt = 0
def channel_change():
    global min_change, cnt
    while queue:
        o = queue.popleft()
        #최소 횟수로 누른 것보다 많으면
        if o[1] > min_change:
            break
        #범위를 벗어나면 continue
        if o[0] < 0:
            continue
        if o[0] > m-1:
            continue
        #n[0]이 target일때 min_ch..와 최소 버튼 조작 횟수로 이동하는 방법의 가짓수 + 1
        if o[0] == 0:
            min_change = o[1]
            cnt += 1

        if queue.count(o) >= 8:
            min_change = -1
            break

        for i in range(len(um)):
            queue.append([(o[0]*um[i][0]+um[i][1])%m,o[1]+1])

m,n,s = map(int,input().split())
um = [list(map(int,input().split())) for _ in range(n)]
# start, target =  map(int, input().split())
queue = deque()
queue.append([s,0])
channel_change()

print(min_change)