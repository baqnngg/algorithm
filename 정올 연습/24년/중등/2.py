# 공 던지기 대회
n = int(input())
r = []
cnt = 0
for i in range(n):
    b = int(input())
    if b >= 20: cnt += 1
    r.append(b)

r.sort(reverse=True)
print(*r,f"\n{cnt}")