import math
m = int(input())
n = int(input())
b = list(map(int,input().split()))
l = m
for i in b:
    kk = (l*i)/100
    l += kk
if l-m < m-l:
    print(math.ceil(l)-m,"\nbad")
elif l == m:
    print(0,"\nsame")
else:
    print(math.ceil(int(m-l)),"\ngood")