# 현명한 소비
k = int(input())
n = int(input())
a = list(map(int,input().split()))
if sum(a) <= k: print("YES")
else: print("NO")