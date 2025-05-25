# 수강 신청
n = int(input())
a = [list(input().split()) for _ in range(n)]
for i in range(n):
    a[i].sort()
for i in range(n):
    res = "".join(a[i])
    a[i] = res
a = set(a)
print(len(a))