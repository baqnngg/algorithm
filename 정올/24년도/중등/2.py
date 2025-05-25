#공 던지기 대회
n = int(input())
m = [int(input()) for _ in range(n)]
cnt = 0

for i in m:
    if i >= 20: cnt += 1

m.sort(reverse=True)

print(*m)
print(cnt)