from collections import deque

def lol():
    minc = 0
    a = m.pop(0)
    while queue:
        n = queue.popleft()

        if n[2] > minc:
            a = m.pop(0)
            minc = n[2]
            
        if n[2] >= kk-2:
            return

        queue.append([n[0]+a,n[1]+[a],n[2]+1])
        ll.append(n[0]+a)
        queue.append([n[0]-a,n[1]+[a],n[2]+1])
        ll.append(n[0]-a)
        queue.append([n[0]*a,n[1]+[a],n[2]+1])
        ll.append(n[0]*a)

n = int(input())
for _ in range(n):
    m = list(map(int,input().split()))
    ll = []
    m.pop(0)
    m.append(0)
    kk = len(m)
    queue = deque()
    Start = m.pop(0)
    queue.append([Start,[Start],0])
    lol()
    print(f"{max(ll)}\n{min(ll)}")