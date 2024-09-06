import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
points = list(map(int,input().split()))
aa = []
for i in range(n):
    if points[i] > 0 and points[i] <= k:
        aa.append(abs((m-1)-i))
if aa != []: 
    print(min(aa)*10)