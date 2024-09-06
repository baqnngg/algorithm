from collections import deque
#처음 min_ch...에서 안막히려고
min_change = 99999
#최소 버튼 조작 횟수로 이동하는 방법의 가짓수
cnt = 0
def channel_change():
    global min_change, cnt
    while queue:
        n = queue.popleft()
        #범위를 벗어나면 continue
        if n[0] < 1:
            continue
        if n[0] > 100000:
            continue
        if n[0] == target:
            min_change = n[1]
            break
        for btn in [1,-1,10]:
            queue.append([n[0]+btn,n[1]+1])
        queue.append([n[0]*5,n[1]+1])

start, target =  map(int, input().split())
queue = deque()
queue.append([start,0])
channel_change()

print(min_change)