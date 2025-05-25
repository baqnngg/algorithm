# 채널을 빨리 바꾸는 방법
from collections import deque

def bfs():
    global minc, cnt
    while q:
        a = q.popleft()
        if minc < len(a[1]):
            break
        if a[0] == t:
            minc = len(a[1])
            cnt += 1
        if a[0] < 1:
            continue
        if a[0] > 40:
            continue
        for i in [-6,-4,-1,3,5,9]:
            q.append([a[0]+i, a[1]+[i]])

c,t = map(int, input().split())
minc = 99999
cnt = 0
q = deque()
q.append([c,[]])
bfs()

print(f"{minc}\n{cnt}")