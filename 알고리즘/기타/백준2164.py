from collections import deque
import sys
input = sys.stdin.readline
a = deque([i for i in range(1,int(input())+1)])
while len(a) > 1:
    a.popleft()
    a.append(a.popleft())
print(a[0])