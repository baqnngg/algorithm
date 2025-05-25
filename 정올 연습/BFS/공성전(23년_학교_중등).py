from itertools import combinations

n,h = map(int,input().split())
ladd = [int(input()) for _ in range(n)]
dif = []

for i in range(1,n+1):
    for j in combinations(ladd,i):
        if sum(j) >= h:
            dif.append(sum(j))
            
print(min(dif)-h)