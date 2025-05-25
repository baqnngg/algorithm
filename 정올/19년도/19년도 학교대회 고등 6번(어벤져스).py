n, ix, iy = map(int,input().split())
m = []
for _ in range(n):
    x,y = map(int,input().split())
    if x - ix == 0: m.append(float('inf'))
    elif y - iy == 0: m.append(0)
    else: m.append((y - iy) / (x - ix))

m = set(m)

print(len(m))