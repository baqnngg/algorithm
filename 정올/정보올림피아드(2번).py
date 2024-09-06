import math
n,m = map(int,input().split())
x,y = map(int,input().split())
d = int(input())
move = math.gcd(n, m)
print(int(n*m//move)*2)