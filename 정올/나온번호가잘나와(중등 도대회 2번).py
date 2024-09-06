n,m,k = map(int,input().split())
num = [0] * (n+1)
for i in range(k):
    o = list(map(int,input().split()))
    for p in o:
        for j in range(n+1):
            if p == j:
                num[j] += 1
                break
for i in range(n+1):
    if num[i] == 0:
        continue
    print(i,num[i])