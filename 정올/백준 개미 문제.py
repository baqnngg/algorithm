n,m = map(int,input().split())
x,y = map(int,input().split())
d = int(input())
x_m = [] 
y_m = []
for i in range(n+1):
    x_m.append(i)
for i in range(n-1,0,-1):
    x_m.append(i)
for i in range(m+1):
    y_m.append(i)
for i in range(m-1,0,-1):
    y_m.append(i)
print(x_m[(d+x_m.index(x))%len(x_m)],y_m[(d+y_m.index(y))%len(y_m)])
#move = math.gcd(n, m)
#print(int(n*m//move)*2)