from collections import deque

#처음 min_ch...에서 안막히려고
min_change = 99999
#최소 버튼 조작 횟수로 이동하는 방법의 가짓수
cnt = 0
def channel_change():
    global min_change, cnt
    while queue:
        n = queue.popleft()
        #최소 횟수로 누른 것보다 많으면
        if n[2] > min_change:
            break
        #범위를 벗어나면 continue
        if n[0] < 1:
            continue
        if n[0] > 40:
            continue
        #n[0]이 target일때 min_ch..와 최소 버튼 조작 횟수로 이동하는 방법의 가짓수 + 1
        if n[0] == target:
            min_change = n[2]
            cnt += 1
        #for문 돌려서 9,5,3,-1,-4,-6 돌리기
        for btn in [9,5,3,-1,-4,-6]:
            queue.append([n[0]+btn,n[1]+[btn],n[2]+1])

start, target =  map(int, input().split())
queue = deque()
queue.append([start,[],0])
channel_change()

print(min_change)
print(cnt)