from collections import deque
import sys

Mincg = sys.maxsize
possible = 0

def bfs():
    global Mincg, possible
    while queue:
        c, cnt = queue.popleft()
        if c == t:
            possible += 1
            Mincg = min(Mincg, cnt)
        if Mincg < cnt: # 탈출 조건
            break
        if c < 1:
            continue
        if c > 40:
            continue
        for i in [-6, -4, -1, 3, 5, 9]:
            queue.append((c + i, cnt + 1))

c, t = map(int, input().split())
queue = deque()
queue.append((c, 0)) # 초기값, 횟수
bfs()
print(f"{Mincg}\n{possible}")