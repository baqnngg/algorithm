n = int(input())
X = map(int,input().split())
Y = map(int,input().split())
s = 0
for i,j in zip(X,Y):
    print((i*j)+s)
    s += i*j