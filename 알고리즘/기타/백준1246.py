n,m = map(int,input().split())
p = [int(input()) for _ in range(m)]
p.sort()
ps = []
for i in range(m):
    if len(p)-i >= n:
        ps.append(p[i] * n)
    else:
        ps.append(p[i]*(len(p)-i))
print(p[ps.index(max(ps))],max(ps))