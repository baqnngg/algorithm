#수강 신청
n = int(input())
m = [list(input().split()) for _ in range(n)]
for i in range(n):
    m[i].sort()
for i in range(n):
    res = "".join(m[i])
    m[i] = res
m = set(m)
print(len(m))