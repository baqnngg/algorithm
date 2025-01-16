xy = []
for _ in range(3):
    a,b = map(int,input().split())
    xy.append([a,b])
ccw = ((xy[0][0]*xy[1][1])+(xy[1][0]*xy[2][1])+(xy[2][0]*xy[0][1]))-((xy[1][0]*xy[0][1])+(xy[2][0]*xy[1][1])+(xy[0][0]*xy[2][1]))
if ccw < 0: print(-1)
elif ccw == 0: print(0)
else: print(1)