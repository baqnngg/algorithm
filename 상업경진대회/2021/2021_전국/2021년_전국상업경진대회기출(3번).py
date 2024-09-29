a,b,c = map(int,input().split())
for i in range(c):
    xy,m = input().split()
    xy = xy.split(',')
    x,y = int(xy[0]),int(xy[1])
    for m in m:
        temp1,temp2 = x,y
        if m == 'L': x-=1
        elif m == 'R': x+=1
        elif m == 'U': y-=1
        elif m == 'D': y+=1
        if x == 0 or x == a+1 or y == 0 or y == b+1: x,y = temp1,temp2
    print(x,y)